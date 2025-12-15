#!/usr/bin/env python3
"""
guess_number.py

Simple interactive "Guess the Number" game.

Features:
- Player guesses a random integer in a range (default 1-100).
- Optional command-line args to set min, max, and max attempts.
- Hints: "higher" or "lower".
- Non-integer inputs are handled (they don't count as attempts).
- Type 'q' or 'quit' to exit during a game.
- Option to play again after each round.

Usage:
    python guess_number.py
    python guess_number.py --min 1 --max 50 --attempts 10
"""
import random
import argparse
import sys

def play_round(low: int, high: int, max_attempts: int | None):
    target = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    if max_attempts:
        print(f"You have up to {max_attempts} attempts to guess it.")
    print("Type 'q' or 'quit' to exit.\n")

    while True:
        prompt = f"Enter your guess ({low}-{high}): "
        user = input(prompt).strip().lower()

        if user in ("q", "quit"):
            print("Goodbye!")
            sys.exit(0)

        try:
            guess = int(user)
        except ValueError:
            print("That's not a valid integer — try again (this won't count as an attempt).")
            continue

        if guess < low or guess > high:
            print(f"Please guess a number between {low} and {high}.")
            continue

        attempts += 1

        if guess == target:
            print(f"Correct! You guessed the number in {attempts} attempt{'s' if attempts != 1 else ''}.\n")
            return True, attempts
        elif guess < target:
            print("My number is higher.")
        else:
            print("My number is lower.")

        if max_attempts and attempts >= max_attempts:
            print(f"Out of attempts! The number was {target}.\n")
            return False, attempts

def main():
    parser = argparse.ArgumentParser(description="Play a guess-the-number game.")
    parser.add_argument("--min", type=int, default=1, help="Minimum number (inclusive).")
    parser.add_argument("--max", type=int, default=100, help="Maximum number (inclusive).")
    parser.add_argument("--attempts", type=int, default=None, help="Maximum attempts (optional).")
    args = parser.parse_args()

    low, high = args.min, args.max
    if low >= high:
        print("Error: --min must be less than --max.")
        sys.exit(1)

    print("Welcome to Guess the Number!")
    while True:
        won, tries = play_round(low, high, args.attempts)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing — goodbye!")
            break

if __name__ == "__main__":
    main()