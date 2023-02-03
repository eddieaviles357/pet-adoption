# flask --debug run

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet, DEFAULT_IMG
from forms import AddPetForm, EditPetForm
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

# GET /


@app.route('/')
def home():
    """ Home page """
    pets = Pet.get_all_pets()
    return render_template("index.html", pets=pets)

# GET /add
# POST /add


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Add pet route """
    form = AddPetForm()
    # import pdb
    # pdb.set_trace()
    species = Pet.get_all_pets_species()
    # if form does not validate or if route is a GET req
    if form.validate_on_submit():
        # get data from client
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        # create a Pet
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        # add Pet to db
        db.session.add(pet)
        db.session.commit()
        # display message to user if it's a success
        flash("Successfully added Pet", "success")
        # form failed to validate
        return redirect("/")
    else:
        return render_template("add-pet.html", form=form)

# GET /[pet-id]
# POST /[pet-id]


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    """ Display details about pet and edit pet details """
    pet = Pet.query.get_or_404(pet_id)
    # prepoluate Edit form
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        # if user leaves photo emtpy a default will be assigned
        pet.photo_url = form.photo_url.data or DEFAULT_IMG
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        # update pet

        db.session.commit()
        flash("Updated successful", "success")
        return redirect("/")
    return render_template("pet-details.html", pet=pet, form=form)
