from flask import Flask
from dynaconf import settings

from .extensions import configuration


def create_app(**config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configuration.init_app(app, **config)

    return app
