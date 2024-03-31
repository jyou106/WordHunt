"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
import nltk
from nltk.corpus import words
nltk.download('words')

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
    return word in WORDS

def randomized() -> None:
    for i in range(len(BOARD)):
        for j in range(len(BOARD[0])):
            BOARD[i][j] = choice(ascii_uppercase)

def pretty_print() -> None:
    pprint.pprint(BOARD)

def get_input() -> tuple[int, int]:
    x: str
    valid: bool = False
    while not valid:
        valid = True
        x = input("Input: ")
        x = x.split(",")
        if len(x) != 2:
            print("Invalid input. Ex: 0,0")
            valid = False
        for char in x:
            if not char.isdigit() or int(char) < 0:
                print("Should contain only nonnegative digits")
                valid = False     

    return (int(x[0]), int(x[1]))

def is_adjacent(left: tuple[int,int], right: tuple[int,int]) -> bool:
    if abs(left[0] - right[0]) <= 1:
        if abs(left[1] - right[1]) <= 1:
            return True
    return False

if __name__ == "__main__":
    main()
