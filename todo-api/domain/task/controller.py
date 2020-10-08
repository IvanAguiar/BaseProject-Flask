from dynaconf import settings
from flask_restful import Resource


class TaskItem(Resource):
    @staticmethod
    def get():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)
