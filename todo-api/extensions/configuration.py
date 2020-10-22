from dynaconf import FlaskDynaconf

from domain import rest_api
from extensions import database


def init_app(app, **config):
    FlaskDynaconf(app)

    database.init_app(app)
    rest_api.init_app(app)

    database.flush_db(app)
