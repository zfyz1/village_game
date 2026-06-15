from flask import Flask
from config import Config
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    socketio.init_app(app)

    from events.user_events import register_user_events
    register_user_events(socketio)

    return app

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)