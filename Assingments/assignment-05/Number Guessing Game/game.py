#!/usr/bin/env python3
import random
import sys
from typing import Tuple

BANNER = """
==============================
   Number Guessing Game 🎯
==============================
"""

LEVELS = {
    "Easy": {"range": (1, 50), "attempts": 10, "hint": True},
    "Medium": {"range": (1, 75), "attempts": 8, "hint": True},
    "Hard": {"range": (1, 100), "attempts": 6, "hint": False},
}

PROGRESSION_ORDER = ["Easy", "Medium", "Hard"]

class GameResult:
    def __init__(self, won: bool, attempts_used: int, score: int, level: str):
        self.won = won
        self.attempts_used = attempts_used
        self.score = score
        self.level = level


def prompt_choice(prompt: str, choices: Tuple[str, ...]) -> str:
    choices_lower = {c.lower(): c for c in choices}
    while True:
        choice = input(f"{prompt} ({'/'.join(choices)}): ").strip().lower()
        if choice in choices_lower:
            return choices_lower[choice]
        print(f"Invalid choice. Please enter one of: {', '.join(choices)}")


def prompt_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        raw = input(f"{prompt} ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            print("Exiting the game. Goodbye!")
            sys.exit(0)
        try:
            val = int(raw)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid integer (or 'q' to quit).")


def difficulty_menu() -> str:
    print("Select difficulty level:")
    for name in PROGRESSION_ORDER:
        cfg = LEVELS[name]
        rmin, rmax = cfg["range"]
        print(f"- {name}: range {rmin}..{rmax}, attempts {cfg['attempts']}, hints {'on' if cfg['hint'] else 'off'}")
    return prompt_choice("Choose", tuple(PROGRESSION_ORDER))


def play_round(level_name: str) -> GameResult:
    cfg = LEVELS[level_name]
    rmin, rmax = cfg["range"]
    attempts = cfg["attempts"]
    secret = random.randint(rmin, rmax)

    # Dynamic hint thresholds
    hot_threshold = max(2, (rmax - rmin) // 20)  # within ~5% of range
    warm_threshold = max(5, (rmax - rmin) // 10) # within ~10% of range

    print(f"\nLevel: {level_name} | Guess a number between {rmin} and {rmax}")
    print(f"You have {attempts} attempts.")
    if cfg["hint"]:
        print("Hints enabled: 'hot', 'warm', 'cold' feedback.")
    print("Type 'q' anytime to quit.")

    low_bound, high_bound = rmin, rmax
    attempts_used = 0

    while attempts_used < attempts:
        print(f"Current range hint: {low_bound}..{high_bound}")
        guess = prompt_int("Enter your guess:", rmin, rmax)
        attempts_used += 1

        if guess == secret:
            # Score: base per level + bonus for remaining attempts
            base_scores = {"Easy": 50, "Medium": 75, "Hard": 100}
            score = base_scores[level_name] + (attempts - attempts_used + 1) * 5
            print(f"Correct! 🎉 You found it in {attempts_used} attempts.")
            print(f"Score for this round: {score}")
            return GameResult(True, attempts_used, score, level_name)

        # Update dynamic bounds
        if guess < secret:
            low_bound = max(low_bound, guess + 1)
            print("Too low.")
        else:
            high_bound = min(high_bound, guess - 1)
            print("Too high.")

        # Proximity hint
        if cfg["hint"]:
            diff = abs(guess - secret)
            if diff <= hot_threshold:
                print("You're hot 🔥")
            elif diff <= warm_threshold:
                print("You're warm 🙂")
            else:
                print("Cold ❄️")

        # Attempts remaining
        remaining = attempts - attempts_used
        if remaining:
            print(f"Attempts left: {remaining}\n")
        else:
            print("No attempts left.")

    print(f"Out of attempts. The number was {secret}.")
    return GameResult(False, attempts_used, 0, level_name)


def next_level(current: str) -> str:
    idx = PROGRESSION_ORDER.index(current)
    if idx + 1 < len(PROGRESSION_ORDER):
        return PROGRESSION_ORDER[idx + 1]
    return current  # stay on Hard


def main():
    print(BANNER)

    # Ask to show instructions
    show_help = prompt_choice("Show instructions?", ("Yes", "No"))
    if show_help == "Yes":
        print("""
How to play:
- Choose a difficulty level.
- Guess a number within the given range.
- You have limited attempts per level.
- Receive feedback whether your guess is too high/low.
- On Easy/Medium, proximity hints (hot/warm/cold) help.
- Win to auto-progress to the next level.
- Type 'q' to exit anytime.
""")

    # Initial difficulty
    current_level = difficulty_menu()

    total_score = 0
    rounds_played = 0

    while True:
        result = play_round(current_level)
        total_score += result.score
        rounds_played += 1

        if result.won:
            next_lvl = next_level(result.level)
            if next_lvl != result.level:
                print(f"Advancing to {next_lvl} difficulty!")
                current_level = next_lvl
            else:
                print("You're at the highest difficulty. Great job!")
        else:
            # On loss, optionally retry same level
            print("Would you like to retry the same level or change?")
            action = prompt_choice("Choose", ("Retry", "Change Level", "Quit"))
            if action == "Retry":
                pass  # keep current_level
            elif action == "Change Level":
                current_level = difficulty_menu()
            else:
                print("Thanks for playing!")
                break

        # After each round, ask to continue
        cont = prompt_choice("Play another round?", ("Yes", "No"))
        if cont == "No":
            break

    print("\n==============================")
    print(f"Rounds played: {rounds_played}")
    print(f"Total score: {total_score}")
    print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")
