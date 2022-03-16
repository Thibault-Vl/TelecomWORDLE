"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/03/2022
"""

# Import needed modules
from typing import Dict, Union
from flask import request, render_template, redirect, Response, Blueprint

# Import personal modules
from app.core.takeRandomWord import takeRandomWord
from app.core.checkWinCondition import checkWinCondition
from app.core.coreFile import read_json

# Import blueprint
from . import mainBlueprint

# Definition of global variable
global requiredWord


# Definition of the tusmo route
@mainBlueprint.route("/", methods=['GET', 'POST'])
@mainBlueprint.route("/tosmu", methods=['GET', 'POST'])
def mainBP_tusmo() -> Union[Response, str, Dict[str, bool]]:
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

        return render_template('home.html', hiddenWord=requiredWord.upper(), tries=tries, wordlength=wordlength)

    elif request.method == 'POST':
        userWord = request.form['word'].lower()
        currentTry = int(request.form['try'])
        data = read_json('config')

        print(userWord, requiredWord)

        data = checkWinCondition(userWord, requiredWord, currentTry, int(data['tries']))

        return data
