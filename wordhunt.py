"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
import time
import enchant


__author__ = "Jessie You"

SIZE = 4
BOARD = [["A"] * SIZE for i in range(SIZE)]
WORDS = enchant.Dict("en_US")


def main() -> None:
    randomized()
    pretty_print()
    play() 


def play() -> None:
    """Play the game"""
    # TODO
    points: int
    user_words: list[str] = []
    duration = 10
    start_time = time.time()
    while int(time.time() - start_time) < duration:
        word: str = get_word()
        print(word)
        if is_word_valid(word):
            user_words.append(word)


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


def get_word() -> str | None:
    """Get a word on the board from the user. The user inputs a list of indices (e.g., 0,0;1,2;1,3)."""
    s: str = ""

    user_input: str = input("Input: ")
    user_input.replace(" ", "")

    if not all(char.isdigit() or char in {",", ";"} for char in user_input) or not user_input:
        print("Invalid input. Ex: 0,0;1,2;1,3 (nonnegative integers)")
        return None

    user_input_split: list[str] = user_input.split(";")
    index_pairs: list[tuple[int, int]] = []

    for index_pair in user_input_split:
        index_pair_int = tuple(map(int, index_pair.split(",")))
        if len(index_pair_int) != 2:
            print(f"{index_pair_int} doesn't have 2 elements. Need pairs of indices (i, j).")
            return None
        if index_pair_int[0] >= SIZE or index_pair_int[1] >= SIZE:
            print(f"{index_pair_int} has out-of-bounds element(s). Both indices must be less than {SIZE}")
            return None
        index_pairs.append(index_pair_int)

    # Should use iterator
    for i in range(0, len(index_pairs) - 1):
        prev_index_pair: tuple[int, int] = index_pairs[i]
        curr_index_pair: tuple[int, int] = index_pairs[i+1]
        if not is_adjacent(prev_index_pair, curr_index_pair):
            print(f"Index pairs {prev_index_pair} and {curr_index_pair} are not adjacent to each other")
            return None

    for index_pair in index_pairs:
        s += BOARD[index_pair[0]][index_pair[1]]
    
    return s

def is_adjacent(left: tuple[int, int], right: tuple[int, int]) -> bool:
    if left == right:
        return False
    if abs(left[0] - right[0]) <= 1 and abs(left[1] - right[1]) <= 1:
        return True
    return False


if __name__ == "__main__":
    main()
