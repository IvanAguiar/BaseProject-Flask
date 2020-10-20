from flask_restful import Api

from .controller import TaskItem
from .controller import TaskItemList


def load_routes(blueprint):
    api = Api(blueprint)
    api.add_resource(TaskItemList, '/tasks')
    api.add_resource(TaskItem, '/task/<int:id>')

