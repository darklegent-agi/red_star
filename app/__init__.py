from flask import Flask
from .database import init_db


def create_app():
    app = Flask(__name__)
    # Load configuration for database and other settings
    app.config.from_object('app.config')
    init_db(app)

    from . import main
    app.register_blueprint(main.bp)

    return app
