"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 13/03/2021
"""

# Import needed package
from flask_socketio import SocketIO

# Import personal package
from app import create_app


# Start app if file is not imported
if __name__ == "__main__":
    app = create_app(debug=True)

    # Config socketIO
    socketio = SocketIO(app)

    # Run app
    socketio.run(app=app, host='0.0.0.0', port=5454)
