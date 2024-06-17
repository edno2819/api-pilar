import os
import logging
from flask import Flask
from flask_cors import CORS
from .cache import cache
from flask.logging import default_handler


def configure_logger(app):
    app.logger.setLevel(logging.INFO)
    app.logger.removeHandler(default_handler)

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s')

    # Log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    app.logger.addHandler(console_handler)

    # Save Log in file
    file_handler = logging.FileHandler('./logs/app.log')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    CORS(app)
    cache.init_app(app)
    configure_logger(app)

    with app.app_context():
        from . import routes

    return app
