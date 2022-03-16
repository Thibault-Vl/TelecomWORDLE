#  Copyright (c) 2022/3/14.

# Import needed package
from typing import Dict


def countWordLetters(word: str) -> Dict[str, int]:
    data = {}

    for letters in word:
        try:
            data[letters] += 1
        except KeyError:
            data[letters] = 1

    return data
