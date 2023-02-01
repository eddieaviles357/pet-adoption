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
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.SmallInteger)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean)

    def __repr__(self):
        """ Model representation """
        return f"<Pet name: {self.name}, species: {self.species}, photo_url: ..., age: {self.age}, notes: ..., available: {self.available}>"

    @classmethod
    def get_all_pets(cls):
        """ Get all pets in database """
        return cls.query.all()

    @classmethod
    def get_all_pets_by_name(cls, name):
        """ Get all pets that matches name """
        return cls.query.filter(name=name).all()

    @classmethod
    def get_all_pets_by_species(cls, species):
        """ Get all pets that matches species """
        return cls.query.filter(species=species).all()

    @classmethod
    def get_all_pets_by_age(cls, age):
        """ Get all pets that matches age """
        return cls.query.filter(age=age).all()

    @classmethod
    def get_all_pets_available(cls, available):
        """ Get all pets available """
        return cls.query.filter(available=available).all()
