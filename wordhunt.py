"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
import nltk
from nltk.corpus import words

try:
    words.words()
except LookupError:
    nltk.download("words")

__author__ = "Jessie You"

SIZE = 4
BOARD = [["A"]*SIZE for i in range(SIZE)]
WORDS = words.words()

def main() -> None:
    randomized()
    pretty_print()
    print(is_word_valid("true"))
    print(is_word_valid("nutzzz"))

def play() -> None:
    """Play the game"""
    # TODO
    pass

def is_word_valid(word: str) -> bool:
    return word.lower() in WORDS

def randomized() -> None:
    for i in range(len(BOARD)):
        for j in range(len(BOARD[0])):
            BOARD[i][j] = choice(ascii_uppercase)

def pretty_print() -> None:
    pprint.pprint(BOARD)

def get_input() -> tuple[int, int]:
    indices: tuple[int, ...]
    while True:
        user_input = input("Input: ")
        user_input = user_input.replace(" ", "")

        if not all(char.isdigit() or char == "," for char in user_input):
            print("Invalid input. Ex: 0, 0 (nonnegative integers)")
            continue

        indices = tuple(map(int, user_input.split(",")))

        if len(indices) != 2:
            print("Invalid number of inputs. Ex: 0, 0")
            continue
        if indices[0] >= SIZE or indices[1] >= SIZE:
            print(f"Invalid input. Both indices must be less than {SIZE}")
            continue

        break

    return indices[0], indices[1]

def is_adjacent(left: tuple[int,int], right: tuple[int,int]) -> bool:
    if abs(left[0] - right[0]) <= 1 and abs(left[1] - right[1]) <= 1:
        return True
    return False

if __name__ == "__main__":
    main()
