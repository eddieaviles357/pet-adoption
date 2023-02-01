# flask --debug run

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm
app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI="postgresql:///adoption",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    # SQLALCHEMY_ECHO=True,
    SECRET_KEY="mensajesecreto",
    DEBUG_TB_INTERCEPT_REDIRECTS=False
)

connect_db(app)
# db.drop_all()
# db.create_all()

# Debug Extension on
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    """ Home page """
    pets = Pet.get_all_pets()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Add pet form """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash("Successfully added Pet", "success")
        return redirect("/")
    else:
        return render_template("add-pet.html", form=form)
