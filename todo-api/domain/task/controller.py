from flask_restful import Resource


class TaskItem(Resource):
    @staticmethod
    def get():
        return {'task': 'Hello, World!'}
