import re
import sys
from argparse import ArgumentParser


HAPPY_WORDS = {
    "happy", "joy", "glad", "delighted", "great", "awesome", "fantastic",
    "love", "amazing", "good", "yay", "excited", "wonderful", "pleased",
    "smile", "lol", "haha", "lmao", "cheerful",
}

SAD_WORDS = {
    "sad", "unhappy", "down", "depressed", "cry", "crying", "tears",
    "terrible", "bad", "upset", "lonely", "miserable", "heartbroken",
    "blue", "unfortunate", "sorrow", "grief", "melancholy",
}

ANGRY_WORDS = {
    "angry", "mad", "furious", "rage", "annoyed", "irritated", "pissed",
    "hate", "disgusted", "outraged", "livid", "wtf", "sucks", "stupid",
    "idiot", "annoying", "furious",
}

HAPPY_EMOJI = {"😀", "😃", "😄", "😁", "😊", "🙂", "🤗", "🥳", "😍", "😂", "🤣", ":)", ":-)", "=)"}
SAD_EMOJI = {"😢", "😭", "😞", "😔", "🙁", "☹️", ":(", "T_T", ";-;", ":-("}
ANGRY_EMOJI = {"😡", "😠", "🤬", ">:[", ">:(", "ಠ_ಠ"}

NEGATIONS = {"not", "no", "never", "isn't", "don't", "doesn't", "didn't", "ain't", "can't", "won't"}


def tokenize(text: str):
    return re.findall(r"[A-Za-z']+|[:;=8xX][-^]?[)D(]|[😀-🙏🤣🥳😡😠🤬😭😢😞😔🙁☹️]", text)


def score_emotion(text: str):
    text_lower = text.lower()

    happy = 0.0
    sad = 0.0
    angry = 0.0

    tokens = tokenize(text)

    def is_caps(word: str):
        return len(word) >= 2 and word.isupper()

    caps_count = sum(1 for t in tokens if t.isalpha() and is_caps(t))

    i = 0
    while i < len(tokens):
        t = tokens[i]
        t_low = t.lower()
        prev_is_neg = (i > 0 and tokens[i - 1].lower() in NEGATIONS)

        if t_low in HAPPY_WORDS:
            happy += 2.0 if not prev_is_neg else -1.5
        elif t_low in SAD_WORDS:
            sad += 2.0 if not prev_is_neg else -1.5
        elif t_low in ANGRY_WORDS:
            angry += 2.0 if not prev_is_neg else -1.5

        # Emoji / emoticons
        if t in HAPPY_EMOJI:
            happy += 2.0
        if t in SAD_EMOJI:
            sad += 2.0
        if t in ANGRY_EMOJI:
            angry += 2.0

        i += 1

    # Exclamation handling: tilt toward the dominant valence or anger if none
    exclamations = text.count("!")
    if exclamations:
        if happy > sad and happy > angry:
            happy += 0.5 * exclamations
        elif sad > happy and sad > angry:
            sad += 0.5 * exclamations
        else:
            angry += 0.5 * exclamations

    # CAPS tends to correlate with anger/emphasis
    if caps_count >= 2:
        angry += 1.0

    return {"happy": happy, "sad": sad, "angry": angry}


def classify(text: str):
    scores = score_emotion(text)
    label = max(scores, key=scores.get)
    top = scores[label]
    # Neutral fallback if all are near zero
    if top <= 0.5:
        return "neutral", scores
    return label, scores


def format_result(label: str):
    emoji = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😠",
        "neutral": "😐",
    }[label]
    return f"{emoji} {label.upper()}"


def main():
    parser = ArgumentParser(description="Classify a sentence as happy, sad, angry (or neutral).")
    parser.add_argument("text", nargs="*", help="Sentence to analyze. If omitted, reads from stdin interactively.")
    args = parser.parse_args()

    if args.text:
        text = " ".join(args.text)
        label, scores = classify(text)
        print(format_result(label))
        return

    try:
        print("=== 😊 Emotion Classifier (happy/sad/angry) ===")
        print("Type 'q' to quit.\n")
        while True:
            line = input("📝 Enter a sentence: ").strip()
            if not line:
                continue
            if line.lower() in {"q", "quit", "exit"}:
                print("👋 Goodbye!")
                break
            label, _ = classify(line)
            print(format_result(label))
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()

