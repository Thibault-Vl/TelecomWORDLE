"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 27/11/2021
"""

#  Copyright (c) 2022/3/14.

# Import needed packages
from pathlib import Path
from typing import List


def get_path(i: int) -> str:
    """
        Function which send back the path of the i parent from the current folder.

        Parameters :
            - i (integer) : index of the parent's path

        Returns :
            - cwd (string) : path of the i parent
    """

    cwd = Path(__file__).parents[i]
    cwd = str(cwd)
    return cwd


def read_file(filename: str, filetype: str, folder: str) -> List:
    cwd = get_path(2)
    cwd += '/data/' + folder + '/' + filename + '.' + filetype

    with open(cwd, 'r') as file:
        data = file.readlines()

    return data
