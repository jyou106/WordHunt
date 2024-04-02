"""Word hunt simulator"""

from string import ascii_uppercase
from random import choice
import pprint
import time
from inputimeout import inputimeout
import enchant
import json
import re


__author__ = "Jessie You"

SIZE = 4
BOARD = [["A"] * SIZE for _ in range(SIZE)]
WORDS = enchant.Dict("en_US")
SCORES: dict[int, int] = {
    3: 100,
    4: 400,
    5: 800,
    6: 1400,
    7: 1800,
    8: 2200,
    9: 2600,
    10: 3000,
    11: 3400,
    12: 3800,
    13: 4200,
    14: 4600,
    15: 5000,
    16: 5400,
}

INDEX_FORMAT: re.Pattern = re.compile(r"(\d*,\d*;)*\d*,\d*")
"""Matches strings such as

* 0,0
* 0,0;1,1
* 0,0;1,1;2,3
"""


def main() -> None:
    randomize_board()
    play()


def play() -> None:
    """Play the game"""
    user_words: list[str] = []
    duration = 35
    start_time = time.time()

    while int(time.time() - start_time) < duration:
        pprint.pprint(BOARD)
        word: str | None = get_word()
        if word is None:
            # don't need to print error message because get_word() already prints one
            continue
        elif is_word_valid(word):
            user_words.append(word)
            print(f"Valid word {word}")
        else:
            print(f"Invalid word {word}")

    sorted_words: list[str] = sorted(
        user_words, key=lambda word: (len(word), word), reverse=True
    )
    words_and_scores: dict[str, int] = {
        word: SCORES[len(word)] for word in sorted_words
    }

    total_words: int = len(user_words)

    print("\n" + json.dumps(words_and_scores, indent=4))
    print(f"Score: {sum(words_and_scores.values())}")
    print(f"Words: {total_words}")


def is_word_valid(word: str) -> bool | None:
    """Return type includes None because `check` could raise error, but this will realistically never happen"""
    if len(word) < 3:
        return False
    return WORDS.check(word)


def randomize_board() -> None:
    for i in range(len(BOARD)):
        for j in range(len(BOARD[0])):
            BOARD[i][j] = choice(ascii_uppercase)


def get_word() -> str | None:
    """Get a word on the board from the user. The user inputs a list of index pairs, such as 0,0;1,2;1,3

    Returns None if the input is invalid."""
    user_input: str = input("Input: ")
    user_input = user_input.replace(" ", "")

    if INDEX_FORMAT.match(user_input) is None:
        print("Invalid input. Ex: 0,0;1,2;1,3 (nonnegative integers)")
        return None

    user_input_split: list[str] = user_input.split(";")
    index_pairs: list[tuple[int, int]] = []

    for index_pair in user_input_split:
        index_pair_tup = tuple(map(int, index_pair.split(",")))
        if index_pair_tup[0] >= SIZE or index_pair_tup[1] >= SIZE:
            print(
                f"{index_pair_tup} has out-of-bounds element(s). Both indices must be less than {SIZE}"
            )
            return None
        # O(N) find in a list, but N is small
        if index_pair_tup in index_pairs:
            print(f"Index pair {index_pair_tup} is repeated")
            return None
        index_pairs.append(index_pair_tup)  # type: ignore

    if not all(
        is_adjacent(index_pairs[i], index_pairs[i + 1])
        for i in range(len(index_pairs) - 1)
    ):
        print("All index pairs must be adjacent to each other")
        return None

    return "".join(BOARD[i][j] for i, j in index_pairs)


def is_adjacent(left: tuple[int, int], right: tuple[int, int]) -> bool:
    if left == right:
        return False
    return abs(left[0] - right[0]) <= 1 and abs(left[1] - right[1]) <= 1


if __name__ == "__main__":
    main()
