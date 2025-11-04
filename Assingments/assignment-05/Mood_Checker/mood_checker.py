#!/usr/bin/env python3
import random
import sys
import re

BANNER = """
=============================
      Mood Checker 😊
=============================
"""

MOOD_KEYWORDS = {
    "happy": ["happy", "glad", "joy", "great", "good", "excited", "grateful", "content"],
    "sad": ["sad", "down", "blue", "unhappy", "cry", "heartbroken", "depressed"],
    "anxious": ["anxious", "nervous", "worried", "uneasy", "panic", "overthinking", "tense"],
    "angry": ["angry", "mad", "furious", "upset", "irritated", "annoyed", "frustrated"],
    "tired": ["tired", "exhausted", "sleepy", "fatigued", "drained", "worn out", "burnt"],
    "stressed": ["stress", "stressed", "overwhelmed", "pressure", "busy"],
    "bored": ["bored", "meh", "dull", "uninterested", "apathetic"],
    "motivated": ["motivated", "driven", "focused", "productive", "determined"],
    "lonely": ["lonely", "alone", "isolated"],
}

RESPONSES = {
    "happy": [
        "Love that energy! Share it with someone today.",
        "Keep riding that positive wave—you’re doing great!",
        "Gratitude grows joy. Name one thing you’re grateful for!",
    ],
    "sad": [
        "It’s okay to feel sad. Be gentle with yourself today.",
        "Small steps count. A short walk or a call with a friend can help.",
        "Your feelings are valid. This moment will pass—hang in there.",
    ],
    "anxious": [
        "Try the 4-7-8 breath: inhale 4, hold 7, exhale 8.",
        "Focus on what you can control—one thing at a time.",
        "You’ve handled tough moments before. You’ve got this.",
    ],
    "angry": [
        "Pause. A few deep breaths can reset the moment.",
        "Channel it: write it down or take a brisk walk.",
        "Respond, don’t react. You’re in control.",
    ],
    "tired": [
        "Rest is productive. Maybe a quick stretch or power nap?",
        "Hydrate, breathe, and take it slow—you’re doing enough.",
        "Your body’s asking for care. Listen kindly.",
    ],
    "stressed": [
        "Break tasks into tiny steps and celebrate each one.",
        "Take a 60-second pause to breathe and reset.",
        "You don’t have to do it all at once.",
    ],
    "bored": [
        "Try something new for 5 minutes—draw, read, or move.",
        "Turn boredom into curiosity: what’s one small experiment today?",
        "A change of scenery can spark ideas. Step outside for a bit.",
    ],
    "motivated": [
        "Nice! Pick the top task and start now.",
        "Momentum loves action—set a 20-minute timer and go!",
        "You’re on fire. Protect your focus and keep moving.",
    ],
    "lonely": [
        "You’re not alone. Reach out—one message can brighten a day.",
        "Connection helps. Consider a call with someone you trust.",
        "Be kind to yourself—your presence matters.",
    ],
    "generic": [
        "Thanks for sharing. You’re doing your best—keep going.",
        "Every day brings a fresh start. You’ve got this.",
        "One small act of care for yourself right now.",
    ],
}


def classify_mood(text: str) -> str:
    t = text.strip().lower()
    # word-boundary match to avoid partial false positives
    for mood, keywords in MOOD_KEYWORDS.items():
        for kw in keywords:
            pattern = rf"\b{re.escape(kw)}\b"
            if re.search(pattern, t):
                return mood
    return "generic"


def main():
    print(BANNER)
    print("Describe your mood in a few words (or 'q' to quit).")

    while True:
        try:
            user = input("Your mood: ").strip()
        except EOFError:
            print("\nGoodbye!")
            sys.exit(0)
        if not user:
            print("Feel free to say a little or a lot—your call.")
            continue
        if user.lower() in {"q", "quit", "exit"}:
            print("Take care. You’ve got this. 👋")
            break

        mood = classify_mood(user)
        choices = RESPONSES.get(mood, RESPONSES["generic"])
        msg = random.choice(choices)
        mood_label = mood.capitalize() if mood != "generic" else "Mood"
        print(f"\n[{mood_label}] {msg}\n")

        again = input("Another check-in? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Stay kind to yourself. Bye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTake care. 👋")
