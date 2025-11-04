(() => {
  const DIFFICULTIES = {
    easy: { min: 1, max: 50, attempts: 10 },
    medium: { min: 1, max: 100, attempts: 7 },
    hard: { min: 1, max: 500, attempts: 8 },
  };

  const dbKey = 'ngg-db-v1';
  const loadDB = () => JSON.parse(localStorage.getItem(dbKey) || '{"users":{}}');
  const saveDB = (db) => localStorage.setItem(dbKey, JSON.stringify(db));

  const hash = (email, pw) => {
    const s = (email.toLowerCase() + ':' + pw);
    let h = 0;
    for (let i = 0; i < s.length; i++) {
      h = (h << 5) - h + s.charCodeAt(i);
      h |= 0;
    }
    return String(h >>> 0);
  };

  const ensureUser = (db, email) => {
    db.users = db.users || {};
    if (!db.users[email]) {
      db.users[email] = {
        password_hash: null,
        stats: {
          games_played: 0,
          wins: 0,
          best_attempts: null,
          current_streak: 0,
          max_streak: 0,
          achievements: [],
        },
      };
    }
    return db.users[email];
  };

  const emailValid = (email) => /[^@\s]+@[^@\s]+\.[^@\s]+/.test(email);

  // Elements
  const authCard = document.getElementById('auth-card');
  const gameCard = document.getElementById('game-card');
  const statsCard = document.getElementById('stats-card');

  const authForm = document.getElementById('auth-form');
  const emailInput = document.getElementById('email');
  const pwInput = document.getElementById('password');
  const authMsg = document.getElementById('auth-message');
  const loginBtn = document.getElementById('login-btn');
  const registerBtn = document.getElementById('register-btn');

  const whoami = document.getElementById('whoami');
  const logoutBtn = document.getElementById('logout');
  const difficultySel = document.getElementById('difficulty');
  const hintsChk = document.getElementById('hints');
  const form = document.getElementById('guess-form');
  const input = document.getElementById('guess');
  const message = document.getElementById('message');
  const attemptsLeftEl = document.getElementById('attempts-left');
  const rangeEl = document.getElementById('range');
  const playAgainBtn = document.getElementById('play-again');
  const progressBar = document.getElementById('progress-bar');

  const gamesEl = document.getElementById('games');
  const winsEl = document.getElementById('wins');
  const bestEl = document.getElementById('best');
  const streakEl = document.getElementById('streak');
  const maxStreakEl = document.getElementById('max-streak');
  const achList = document.getElementById('achievements');

  let db = loadDB();
  let sessionEmail = null;
  let target = null;
  let attempts = 0;
  let attemptsLeft = 0;
  let bounds = { min: 1, max: 100 };

  const setMessage = (text, cls) => {
    message.textContent = text;
    message.className = `message ${cls || ''}`.trim();
  };

  const resetRound = () => {
    const cfg = DIFFICULTIES[difficultySel.value];
    bounds = { min: cfg.min, max: cfg.max };
    target = Math.floor(Math.random() * (cfg.max - cfg.min + 1)) + cfg.min;
    attempts = 0;
    attemptsLeft = cfg.attempts;
    rangeEl.textContent = `Range: ${cfg.min}-${cfg.max}`;
    attemptsLeftEl.textContent = `Attempts left: ${attemptsLeft}`;
    setMessage('Make your first guess!', '');
    input.value = '';
    input.min = String(cfg.min);
    input.max = String(cfg.max);
    playAgainBtn.hidden = true;
    input.disabled = false;
    form.querySelector('button[type="submit"]').disabled = false;
    progressBar.style.width = '0%';
    input.focus();
  };

  const updateStats = (won, attemptsUsed, elapsedSec) => {
    const user = ensureUser(db, sessionEmail);
    const s = user.stats;
    s.games_played += 1;
    if (won) {
      s.wins += 1;
      s.current_streak += 1;
      s.max_streak = Math.max(s.max_streak, s.current_streak);
      s.best_attempts = s.best_attempts == null ? attemptsUsed : Math.min(s.best_attempts, attemptsUsed);
    } else {
      s.current_streak = 0;
    }

    const ach = new Set(s.achievements || []);
    if (s.wins >= 1) ach.add('First Win');
    if (won && attemptsUsed === 1) ach.add('Flawless Victory');
    if (s.games_played >= 5) ach.add('Persistence');
    if (won && attemptsUsed <= 3) ach.add('Sharpshooter');
    if (won && difficultySel.value === 'hard') ach.add('Hard Mode Clear');
    if (won && elapsedSec <= 10) ach.add('Speedster');
    s.achievements = Array.from(ach).sort();

    saveDB(db);
  };

  const renderStats = () => {
    const user = ensureUser(db, sessionEmail);
    const s = user.stats;
    gamesEl.textContent = s.games_played;
    winsEl.textContent = s.wins;
    bestEl.textContent = s.best_attempts == null ? '-' : s.best_attempts;
    streakEl.textContent = s.current_streak;
    maxStreakEl.textContent = s.max_streak;
    achList.innerHTML = '';
    (s.achievements || []).forEach(a => {
      const li = document.createElement('li');
      li.textContent = a;
      achList.appendChild(li);
    });
  };

  const hintMessage = (guess, target) => {
    const diff = Math.abs(guess - target);
    if (diff === 0) return 'Correct!';
    if (diff <= 3) return 'Very hot!';
    if (diff <= 7) return 'Warm.';
    if (diff <= 15) return 'Cool.';
    return 'Cold.';
  };

  const extraHint = (attemptNum, target) => {
    if (attemptNum === 2) return `Hint: The number is ${target % 2 === 0 ? 'even' : 'odd'}.`;
    if (attemptNum === 4) {
      const facts = [3, 5, 7].filter(n => target % n === 0);
      if (facts.length) return `Hint: Divisible by ${facts.join(', ')}.`;
    }
    return '';
  };

  const setAuthState = (email) => {
    sessionEmail = email;
    if (email) {
      whoami.textContent = email;
      authCard.hidden = true;
      gameCard.hidden = false;
      statsCard.hidden = false;
      resetRound();
      renderStats();
    } else {
      authCard.hidden = false;
      gameCard.hidden = true;
      statsCard.hidden = true;
      whoami.textContent = '';
    }
  };

  registerBtn.addEventListener('click', () => {
    const email = emailInput.value.trim();
    const pw = pwInput.value.trim();
    authMsg.textContent = '';
    db = loadDB();
    if (!emailValid(email)) { authMsg.textContent = 'Invalid email.'; return; }
    if (pw.length < 4) { authMsg.textContent = 'Password too short (min 4).'; return; }
    const user = ensureUser(db, email);
    if (user.password_hash) { authMsg.textContent = 'Account exists. Login instead.'; return; }
    user.password_hash = hash(email, pw);
    saveDB(db);
    authMsg.textContent = 'Registered. You can login now.';
  });

  authForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = emailInput.value.trim();
    const pw = pwInput.value.trim();
    authMsg.textContent = '';
    db = loadDB();
    if (!emailValid(email)) { authMsg.textContent = 'Invalid email.'; return; }
    const user = ensureUser(db, email);
    if (!user.password_hash) { authMsg.textContent = 'No account. Register first.'; return; }
    if (user.password_hash !== hash(email, pw)) { authMsg.textContent = 'Incorrect password.'; return; }
    setAuthState(email);
  });

  logoutBtn.addEventListener('click', () => setAuthState(null));
  difficultySel.addEventListener('change', resetRound);

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const val = Number(input.value);
    if (!Number.isFinite(val)) { setMessage('Please enter a valid number.', 'warn'); return; }
    if (val < bounds.min || val > bounds.max) { setMessage(`Your guess must be between ${bounds.min} and ${bounds.max}.`, 'warn'); return; }

    attempts += 1;
    attemptsLeft -= 1;
    attemptsLeftEl.textContent = `Attempts left: ${attemptsLeft}`;
    const usedPct = Math.min(100, Math.round((attempts / (attempts + attemptsLeft)) * 100));
    progressBar.style.width = `${usedPct}%`;

    if (val < target) {
      setMessage('Too low! Try again.', 'low');
    } else if (val > target) {
      setMessage('Too high! Try again.', 'high');
    } else {
      const elapsed = attempts; // proxy in web (no timer for simplicity)
      setMessage(`Correct! You guessed it in ${attempts} attempt(s).`, 'win');
      updateStats(true, attempts, 0);
      renderStats();
      playAgainBtn.hidden = false;
      input.disabled = true;
      form.querySelector('button[type="submit"]').disabled = true;
      return;
    }

    if (hintsChk.checked) {
      setMessage(`${message.textContent} ${hintMessage(val, target)}`, message.className.replace('message ', ''));
      const eh = extraHint(attempts, target);
      if (eh) setMessage(`${message.textContent} ${eh}`, message.className.replace('message ', ''));
    }

    if (attemptsLeft <= 0) {
      setMessage(`Out of attempts! The number was ${target}.`, 'warn');
      updateStats(false, attempts, 0);
      renderStats();
      playAgainBtn.hidden = false;
      input.disabled = true;
      form.querySelector('button[type="submit"]').disabled = true;
    }
  });

  playAgainBtn.addEventListener('click', resetRound);
})();
