"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 27/11/2021
"""

#  Copyright (c) 2022/3/14.

# Import needed packages
from pathlib import Path
from typing import List
import json


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


def read_json(filename: str) -> dict:
    """
           Function to read a json file

           Parameters :
               - filename (string) : filename

           Returns :
               - data (dict) : data stored in the json file
    """

    cwd = get_path(2)
    cwd += '/data/json/' + filename + '.' + 'json'

    with open(cwd, 'r') as file:
        data = json.load(file)

    return data


def write_json(data: dict, filename: str) -> None:
    """
        Function to modify a json file.

        Parameters :
            - data (dict) : modification of the json file
            - filename (string) : name of the json file to modify

        Returns :
            None
    """

    cwd = get_path(2)

    with open(cwd + '/data/json/' + filename + '.json', 'w') as file:
        json.dump(data, file, indent=4)
