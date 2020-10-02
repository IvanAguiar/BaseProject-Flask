from flask_restful import Api

from .controller import TaskItem


def load_routes(blueprint):
    api = Api(blueprint)
    api.add_resource(TaskItem, '/task')

