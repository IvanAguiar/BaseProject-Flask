from flask import Flask

from .extensions import configuration


def create_app(**config):
    app = Flask(__name__)

    configuration.init_app(app, **config)

    return app
