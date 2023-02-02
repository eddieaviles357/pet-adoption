from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://images.unsplash.com/photo-1574671652898-fc04f34c7517?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1524&q=80"


def connect_db(app):
    """ Connect database """
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet model """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, default=DEFAULT_IMG)
    age = db.Column(db.SmallInteger)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """ Model representation """
        return f"<Pet name: {self.name}, species: {self.species}, photo_url: {self.photo_url}, age: {self.age}, notes: {self.notes}, available: {self.available}>"

    @classmethod
    def get_all_pets(cls):
        """ Get all pets in database """
        return cls.query.all()

    @classmethod
    def get_all_pets_by_name(cls, name):
        """ Get all pets that matches name """
        return cls.query.filter(name=name).all()

    @classmethod
    def get_all_pets_species(cls):
        """ Get all pet species """
        return cls.query.with_entities(Pet.species).all()

    @classmethod
    def get_all_pets_by_species(cls, species):
        """ Get all pets that matches species """
        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_pets_by_age(cls, age):
        """ Get all pets that matches age """
        return cls.query.filter_by(age=age).all()

    @classmethod
    def get_all_pets_available(cls, available):
        """ Get all pets available """
        # must be True or False
        return cls.query.filter_by(available=available).all()
