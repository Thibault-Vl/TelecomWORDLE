"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 13/03/2021
"""

# Import needed packages
from flask import Flask, redirect, flash


# Import personal modules


# Definition of the app
def create_app() -> Flask:
    tosmuApp = Flask(__name__)

    tosmuApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    tosmuApp.config['SECRET_KEY'] = '9e63edf6e48cebb78fe2f533'

    # Import blueprints
    ## Import main blueprint
    from Python.blueprints.mainBP import mainBP
    tosmuApp.register_blueprint(mainBP)

    # Error 404 handler
    @tosmuApp.errorhandler(404)
    def pageNotFound():
        flash("HTTP 404 Not Found", "Red_flash")
        return redirect('/')

    return tosmuApp


# Start app if file is not imported
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5454)
