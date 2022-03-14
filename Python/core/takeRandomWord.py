#  Copyright (c) 2022/3/14.


# Import needed package
import random
from unidecode import unidecode

# Import personal package
from Python.core.coreFile import read_file


def takeRandomWord(wordlength: int):
    data = read_file("gutenberg", "txt", "txt")
    random.shuffle(data)

    for item in data:
        if len(item) == wordlength + 1:
            return unidecode(item[:-1])