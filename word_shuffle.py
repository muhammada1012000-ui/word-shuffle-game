#!/usr/bin/env python3
"""Word Shuffle - a simple terminal word-unscramble game."""

import random

WORDS = {
    "easy": ["apple", "chair", "river", "plant", "bread", "cloud", "tiger", "smile", "house", "water"],
    "medium": ["balance", "journal", "account", "payroll", "invoice", "network", "monitor", "holiday", "freedom", "kitchen"],
    "hard": ["reconciliation", "depreciation", "liability", "compliance", "accountant", "spreadsheet", "efficiency", "adventure", "mountainous", "photography"],
}

MAX_ATTEMPTS = 3
ROUNDS = 5


def shuffle_word(word: str) -> str:
    """Return a shuffled version of the word that differs from the original."""
    letters = list(word)
    while True:
        random.shuffle(letters)
        shuffled = "".join(letters)
        if shuffled != word:
            return shuffled


def choose_difficulty() -> str:
    while True:
        choice = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if choice in WORDS:
            return choice
        print("Please type easy, medium or hard.")


def play_round(word: str, round_no: int) -> int:
    """Play one round. Returns points earned."""
    scrambled = shuffle_word(word)
    points = 10
    hint_used = False

    print(f"\nRound {round_no}/{ROUNDS}")
    print(f"Unscramble:  {scrambled.upper()}")
    print("(type 'hint' for the first letter, 'skip' to skip)")

    attempts = MAX_ATTEMPTS
    while attempts > 0:
        guess = input(f"Your guess [{attempts} left]: ").strip().lower()

        if guess == "skip":
            print(f"Skipped. The word was: {word}")
            return 0
        if guess == "hint":
            if hint_used:
                print("You've already used the hint.")
            else:
                hint_used = True
                points -= 3
                print(f"Hint: starts with '{word[0].upper()}' ({len(word)} letters)")
            continue
        if guess == word:
            earned = max(points - (MAX_ATTEMPTS - attempts) * 2, 1)
            print(f"Correct! +{earned} points")
            return earned

        attempts -= 1
        if attempts:
            print("Not quite, try again.")

    print(f"Out of attempts. The word was: {word}")
    return 0


def main() -> None:
    print("=" * 40)
    print("          WORD SHUFFLE")
    print("=" * 40)

    while True:
        difficulty = choose_difficulty()
        words = random.sample(WORDS[difficulty], ROUNDS)
        score = 0

        for i, word in enumerate(words, start=1):
            score += play_round(word, i)

        print("\n" + "-" * 40)
        print(f"Game over! Final score: {score}/{ROUNDS * 10}")
        print("-" * 40)

        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
