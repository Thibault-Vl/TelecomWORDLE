"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/03/2022
"""

# Import needed modules
from typing import Dict, Union
from flask import Blueprint, request, render_template, redirect, Response

# Import personal modules
from Python.core.takeRandomWord import takeRandomWord
from Python.core.checkWinCondition import checkWinCondition
from Python.core.coreFile import read_json

# Definition of global variable
global requiredWord

# Definition of the blueprint
mainBP = Blueprint("mainBP", __name__)


# Definition of the home route
@mainBP.route('/')
@mainBP.route('/tosmu', methods=['GET', 'POST'])
def mainBP_home() -> Union[Response, str, Dict[str, bool]]:
    global requiredWord

    if request.method == 'GET':
        data = read_json('config')

        try:
            wordlength = int(request.args['wordlength'])

            if wordlength != int(data['wordlength']):
                raise KeyError

        except KeyError:
            wordlength = int(data['wordlength'])
            return redirect(f"/tosmu?wordlength={wordlength}")

        tries = data['tries']

        requiredWord = takeRandomWord(wordlength)

        return render_template('home.html', hiddenWord=requiredWord.upper(), tries=tries)

    elif request.method == 'POST':
        userWord = request.form['word'].lower()
        currentTry = int(request.form['try'])

        print(userWord, requiredWord)

        data = checkWinCondition(userWord, requiredWord, currentTry)

        return data
