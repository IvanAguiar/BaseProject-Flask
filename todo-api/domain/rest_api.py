from flask import Blueprint

from . import task

blueprint = Blueprint('rest_api', __name__, url_prefix="/api")


def init_app(app):
    task.load_routes(blueprint)

    app.register_blueprint(blueprint)
