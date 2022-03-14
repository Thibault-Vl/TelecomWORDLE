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
        try:
            wordLength = int(request.args['wordlength'])
            requiredWord = takeRandomWord(wordLength)
        except KeyError:
            return redirect('/tosmu?wordlength=5')

        return render_template('home.html', hiddenWord=requiredWord.upper())

    elif request.method == 'POST':
        userWord = request.form['word'].lower()
        currentTry = int(request.form['try'])

        print(userWord, requiredWord)

        data = checkWinCondition(userWord, requiredWord, currentTry)

        return data
