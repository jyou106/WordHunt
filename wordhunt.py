"""Word hunt simulator"""

import time
import enchant
import json
import re
from inputimeout import inputimeout, TimeoutOccurred
import numpy as np
from random import choice


__author__ = "Jessie You"

SIZE = 4
BOARD: np.ndarray = np.zeros((4, 4))
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
DURATION: float = 60.0
"""seconds"""
START_TIME: float = 0.0
"""seconds"""

INDEX_FORMAT: re.Pattern = re.compile(r"(\d*,\d*;)*\d*,\d*")
"""Matches strings such as

* 0,0
* 0,0;1,1
* 0,0;1,1;2,3
"""
PROMPT: str = ">> "

# https://boardgames.stackexchange.com/questions/29264/boggle-what-is-the-dice-configuration-for-boggle-in-various-languages
BOGGLE_DISTRIBUTION_4: np.ndarray = np.array(
    [
        ["RIFOBX", "IFEHEY", "DENOWS", "UTOKND"],
        ["HMSRAO", "LUPETS", "ACITOA", "YLGKUE"],
        ["QBMJOA", "EHISPN", "VETIGN", "BALIYT"],
        ["EZAVND", "RALESC", "UWILRG", "PACEMD"],
    ]
)


def main() -> None:
    randomize_board()
    play()


def play() -> None:
    """Play the game"""
    words: dict[str, int] = dict()
    """word: score"""

    global BOARD
    BOARD = randomize_board()

    global START_TIME
    START_TIME = time.time()

    try:
        while True:
            print("\n" + pretty_board(BOARD))
            print(f"{round(DURATION - elapsed_time_seconds())} seconds left")
            word: str | None = get_word()
            if word is None:
                # don't need to print error message because get_word() already prints one
                continue
            elif word in words:
                print(f"Word {word} already found")
            elif is_word_valid(word):
                words[word] = SCORES[len(word)]
                print(f"Valid word {word}")
            else:
                print(f"Invalid word {word}")
    except TimeoutOccurred:
        print("\nTime's up")

    # Sort by negative score (so that higher score appears first), then alphabetically by word
    # Don't use reverse=True because that would make the words appear in reverse alphabetical order
    sorted_words: dict[str, int] = dict(
        sorted(words.items(), key=lambda kv: (-kv[1], kv[0]))
    )

    total_words: int = len(words)

    print("\n" + json.dumps(sorted_words, indent=4))
    print(f"Score: {sum(sorted_words.values())}")
    print(f"Words: {total_words}")


def pretty_board(arr: np.ndarray) -> str:
    return (
        arr.__str__()
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("\n ", "\n")
    )


def is_word_valid(word: str) -> bool | None:
    """Return type includes None because `check` could raise error, but this will realistically never happen"""
    if len(word) < 3:
        return False
    return WORDS.check(word)


def randomize_board() -> np.ndarray:
    return np.reshape(
        np.array(list(map(choice, np.array(BOGGLE_DISTRIBUTION_4.flatten())))),
        BOGGLE_DISTRIBUTION_4.shape,
    )


def get_word() -> str | None:
    """Get a word on the board from the user. The user inputs a list of index pairs, such as 0,0;1,2;1,3

    Returns:
        str | None: The word if it is valid, None otherwise
    Raises:
        TimeoutOccurred: If time has run out
    """
    user_input: str = inputimeout(
        prompt=PROMPT, timeout=(DURATION - elapsed_time_seconds())
    )
    user_input = user_input.replace(" ", "")

    if INDEX_FORMAT.match(user_input) is None:
        print("Invalid input. Ex: 0,0;1,2;1,3 (nonnegative integers)")
        return None

    user_input_split: list[str] = user_input.split(";")
    index_pairs: list[tuple[int, int]] = []

    for index_pair in user_input_split:
        index_pair_tup: tuple[int, int] = tuple(map(int, index_pair.split(",")))  # type: ignore
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


def elapsed_time_seconds() -> float:
    return time.time() - START_TIME


if __name__ == "__main__":
    main()
