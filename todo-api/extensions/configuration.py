from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy

from ..domain import rest_api

db = SQLAlchemy()


def init_app(app, **config):
    FlaskDynaconf(app)

    db.init_app(app)

    rest_api.init_app(app)
