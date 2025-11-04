Number Guessing Game — Features

CLI (main.py)
- Login/Register with email + password (local users.json)
- Difficulty levels: Easy (1-50, 10 attempts), Medium (1-100, 7), Hard (1-500, 8)
- Limited attempts with remaining counter
- Optional hints: temperature hints + parity/divisibility extras
- Stats: games, wins, best attempts, streak and max streak
- Achievements: First Win, Flawless Victory, Persistence, Sharpshooter, Hard Mode Clear, Speedster

Usage (CLI)
- Run: `python main.py`
- Choose Register to create an account, then Login
- Pick difficulty, optionally enable hints, play rounds
- Logout or exit when done

Web (web/index.html)
- Login/Register stored in localStorage
- Difficulty selector, hints toggle, attempts left, range display
- Progress bar of attempts used
- Stats + achievements view
- Play again button

Open `web/index.html` in a browser to play.
