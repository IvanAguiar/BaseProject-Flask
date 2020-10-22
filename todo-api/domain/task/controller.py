import json

from dynaconf import settings
from flask import jsonify
from flask_restful import Resource

from .model import TaskEntity


class TaskItem(Resource):
    @staticmethod
    def get(identifier):
        query = TaskEntity.query.filter_by(id=identifier).first()
        return jsonify({
            'data': query.serialize
        })

    @staticmethod
    def put():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)

    @staticmethod
    def patch():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)

    @staticmethod
    def delete():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)


class TaskItemList(Resource):
    @staticmethod
    def get():
        query = TaskEntity.query.all()
        return jsonify({
            'data': [result.serialize for result in query]
        })

    @staticmethod
    def post():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)

    @staticmethod
    def delete():
        return "Welcome to the %s App! You're using the %s Environment!" % (settings.APP_NAME, settings.ENV_NAME)
