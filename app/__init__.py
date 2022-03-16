"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 13/03/2021
"""

# Import needed package
from flask import Flask, flash, redirect
import os
from werkzeug.exceptions import NotFound


# Definition of the app
def create_app(debug=False) -> Flask:
    template_dir = os.path.abspath('Templates')
    static_dir = os.path.abspath('Static')

    tosmuApp = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Config the app
    tosmuApp.debug = debug

    tosmuApp.config['EXPLAIN_TEMPLATE_LOADING'] = False
    tosmuApp.config['SECRET_KEY'] = '9e63edf6e48cebb78fe2f533'

    # Import blueprints
    # Import main blueprint
    from app.blueprints.mainBP.mainBP import mainBlueprint
    tosmuApp.register_blueprint(mainBlueprint)

    # Import config blueprint
    from app.blueprints.configBP.configBP import configBlueprint
    tosmuApp.register_blueprint(configBlueprint)

    @tosmuApp.errorhandler(404)
    def handleError(e: NotFound):
        flash("Error - 404 Not Found", "Errors")
        return redirect("/tosmu")

    return tosmuApp
