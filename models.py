from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """ Connect database """
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet model """

    __table__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
