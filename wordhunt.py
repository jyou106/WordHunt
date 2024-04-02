"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
from inputimeout import inputimeout
import time
import enchant


__author__ = "Jessie You"

SIZE = 4
BOARD = [["A"] * SIZE for i in range(SIZE)]
WORDS = enchant.Dict("en_US")


def main() -> None:
    #randomized()
    play() 


def play() -> None:
    """Play the game"""
    # TODO
    points: int
    user_word = []
    duration = 10
    start_time = time.time()
    while int(time.time() - start_time) < (duration):
        try: 
        # Take timed input using inputimeout() function 
            time_over = inputimeout(prompt='Name your best friend:', timeout=(duration - (time.time() - start_time))) 
            user_word.append(time_over)
        # Catch the timeout error 
        except Exception: 
            # Declare the timeout statement 
            time_over = 'Your time is over!'
            print(time_over)
    
    print(user_word)


def is_word_valid(word: str) -> bool | None:
    """Return type includes None because `check` could raise error, but this will realistically never happen"""
    # check does not care about case
    return WORDS.check(word)


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
