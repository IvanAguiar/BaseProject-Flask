from flask import Flask

from .domain import rest_api
from .extensions import configuration


def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    configuration.load(app)

    rest_api.init_app(app)

    return app
