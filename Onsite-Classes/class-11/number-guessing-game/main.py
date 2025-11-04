import json
import os
import re
import time
import random
import hashlib

DB_PATH = os.path.join(os.path.dirname(__file__), "users.json")


def load_db():
    if not os.path.exists(DB_PATH):
        return {"users": {}}
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"users": {}}


def save_db(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2)


def email_valid(email: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))


def hash_pw(email: str, password: str) -> str:
    salted = (email.lower().strip() + ":" + password).encode("utf-8")
    return hashlib.sha256(salted).hexdigest()


def ensure_user(db, email):
    users = db.setdefault("users", {})
    if email not in users:
        users[email] = {
            "password_hash": None,
            "stats": {
                "games_played": 0,
                "wins": 0,
                "best_attempts": None,
                "current_streak": 0,
                "max_streak": 0,
                "achievements": [],
            },
        }
    return users[email]


def register(db):
    print("\n=== Register ===")
    while True:
        email = input("Email: ").strip()
        if email.lower() in {"q", "quit", "exit"}:
            return None
        if not email_valid(email):
            print("Invalid email. Try again or type 'q' to quit.")
            continue
        users = db.setdefault("users", {})
        if email in users and users[email]["password_hash"]:
            print("Account already exists. Please login.")
            return None
        password = input("Password: ").strip()
        if len(password) < 4:
            print("Password too short (min 4 chars).")
            continue
        user = ensure_user(db, email)
        user["password_hash"] = hash_pw(email, password)
        save_db(db)
        print("Registration successful. You can now login.")
        return email


def login(db):
    print("\n=== Login ===")
    email = input("Email: ").strip()
    if not email_valid(email):
        print("Invalid email format.")
        return None
    password = input("Password: ").strip()
    users = db.setdefault("users", {})
    if email not in users or not users[email]["password_hash"]:
        print("No account found. Please register first.")
        return None
    if users[email]["password_hash"] != hash_pw(email, password):
        print("Incorrect password.")
        return None
    print(f"Welcome, {email}!")
    return email


DIFFICULTIES = {
    "easy": {"min": 1, "max": 50, "attempts": 10},
    "medium": {"min": 1, "max": 100, "attempts": 7},
    "hard": {"min": 1, "max": 500, "attempts": 8},
}


def choose_difficulty():
    print("\nChoose difficulty:")
    print("  1) Easy   (1-50, 10 attempts)")
    print("  2) Medium (1-100, 7 attempts)")
    print("  3) Hard   (1-500, 8 attempts)")
    while True:
        choice = input("Enter 1/2/3: ").strip()
        mapping = {"1": "easy", "2": "medium", "3": "hard"}
        if choice in mapping:
            return mapping[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def update_stats_on_result(db, email, won: bool, attempts_used: int, difficulty: str, elapsed_sec: float):
    user = ensure_user(db, email)
    stats = user["stats"]
    stats["games_played"] += 1
    if won:
        stats["wins"] += 1
        stats["current_streak"] += 1
        stats["max_streak"] = max(stats["max_streak"], stats["current_streak"])
        if stats["best_attempts"] is None:
            stats["best_attempts"] = attempts_used
        else:
            stats["best_attempts"] = min(stats["best_attempts"], attempts_used)
    else:
        stats["current_streak"] = 0

    ach = set(stats.get("achievements", []))
    if stats["wins"] >= 1:
        ach.add("First Win")
    if won and attempts_used == 1:
        ach.add("Flawless Victory")
    if stats["games_played"] >= 5:
        ach.add("Persistence")
    if won and attempts_used <= 3:
        ach.add("Sharpshooter")
    if won and difficulty == "hard":
        ach.add("Hard Mode Clear")
    if won and elapsed_sec <= 10:
        ach.add("Speedster")
    stats["achievements"] = sorted(ach)

    save_db(db)


def hint_message(guess: int, target: int) -> str:
    diff = abs(guess - target)
    if diff == 0:
        return "Correct!"
    if diff <= 3:
        return "Very hot!"
    if diff <= 7:
        return "Warm."
    if diff <= 15:
        return "Cool."
    return "Cold."


def extra_hint(attempt_num: int, target: int) -> str:
    if attempt_num == 2:
        return f"Hint: The number is {'even' if target % 2 == 0 else 'odd'}."
    if attempt_num == 4:
        facts = []
        for n in (3, 5, 7):
            if target % n == 0:
                facts.append(str(n))
        if facts:
            return f"Hint: Divisible by {', '.join(facts)}."
    return ""


def play_game(difficulty: str, email: str, db):
    cfg = DIFFICULTIES[difficulty]
    low, high, max_attempts = cfg["min"], cfg["max"], cfg["attempts"]
    target = random.randint(low, high)
    attempts = 0
    attempts_left = max_attempts

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print("Type 'q' to quit the round at any time.")
    use_hints = input("Enable hints? (y/n): ").strip().lower() in {"y", "yes"}

    start = time.time()
    while attempts_left > 0:
        raw = input(f"Enter your guess ({attempts_left} attempt(s) left): ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            update_stats_on_result(db, email, won=False, attempts_used=attempts, difficulty=difficulty, elapsed_sec=time.time() - start)
            return False
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not low <= guess <= high:
            print(f"Your guess must be between {low} and {high}.")
            continue

        attempts += 1
        attempts_left -= 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            elapsed = time.time() - start
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            print(f"Time: {elapsed:.1f}s")
            update_stats_on_result(db, email, won=True, attempts_used=attempts, difficulty=difficulty, elapsed_sec=elapsed)
            return True

        if use_hints:
            print(hint_message(guess, target))
            eh = extra_hint(attempts, target)
            if eh:
                print(eh)

    print(f"Out of attempts! The number was {target}.")
    update_stats_on_result(db, email, won=False, attempts_used=attempts, difficulty=difficulty, elapsed_sec=time.time() - start)
    return True


def show_stats(db, email):
    user = ensure_user(db, email)
    s = user["stats"]
    print("\n=== Stats ===")
    print(f"Games: {s['games_played']} | Wins: {s['wins']} | Best Attempts: {s['best_attempts'] or '-'}")
    print(f"Streak: {s['current_streak']} (max {s['max_streak']})")
    if s.get("achievements"):
        print("Achievements:")
        print(" - " + "\n - ".join(s["achievements"]))


def main():
    print("=== Number Guessing Game ===")
    db = load_db()

    while True:
        print("\n1) Login\n2) Register\n3) Quit")
        act = input("Choose: ").strip()
        if act == "1":
            email = login(db)
        elif act == "2":
            email = register(db) or None
            if email:
                pass
            continue
        elif act == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.")
            continue

        if not email:
            continue

        while True:
            show_stats(db, email)
            diff = choose_difficulty()
            finished = play_game(diff, email, db)
            if finished is False:
                pass
            again = input("Play another round? (y/n/logout): ").strip().lower()
            if again in {"logout", "l"}:
                print("Logged out.")
                break
            if again not in {"y", "yes"}:
                print("Thanks for playing!")
                return


if __name__ == "__main__":
    main()
