from flask import Blueprint

blueprint = Blueprint('rest_api', __name__, url_prefix="/api")


def init_app(app):
    from . import task
    task.load_routes(blueprint)

    app.register_blueprint(blueprint)
