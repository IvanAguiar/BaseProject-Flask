from extensions.configuration import db
from sqlalchemy_serializer import SerializerMixin


class TaskEntity(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(1024), unique=True, nullable=False)

    def __repr__(self):
        return '<TaskEntity %r>' % self.title