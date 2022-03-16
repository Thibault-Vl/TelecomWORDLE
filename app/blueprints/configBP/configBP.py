#  Copyright (c) 2022/3/16.

# Import blueprint
from werkzeug import Response

from . import configBlueprint

# Import needed package
from flask import request, flash, redirect
from typing import Union, Dict

# Import personal package
from app.core.coreFile import read_json, write_json


@configBlueprint.route("/modify-config", methods=['POST'])
def configBP_modifyConfig() -> Union[Response, Dict[str, bool]]:
    if request.method == 'GET':
        flash("Error - Method GET not allowed", "Errors")
        return redirect("/")

    elif request.method == 'POST':
        data = read_json("config")

        maxletters = request.form['maxletters']
        data['wordlength'] = maxletters

        write_json(data=data, filename="config")

        return {'statement': True}
