"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
import nltk
from nltk.corpus import words
import time

try:
    words.words()
except LookupError:
    nltk.download("words")

__author__ = "Jessie You"

SIZE = 4
BOARD = [["A"] * SIZE for i in range(SIZE)]
WORDS = words.words()


def main() -> None:
    randomized()
    play()


def play() -> None:
    """Play the game"""
    # TODO
    points: int
    array = []
    time_start = time.now()
    while (time.now() - time_start).totalseconds() < 180:
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

def is_adjacent(left: tuple[int, int], right: tuple[int, int]) -> bool:
    if left == right:
        return False
    if abs(left[0] - right[0]) <= 1 and abs(left[1] - right[1]) <= 1:
        return True
    return False


if __name__ == "__main__":
    main()
