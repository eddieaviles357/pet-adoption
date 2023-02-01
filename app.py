# flask --debug run

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet

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
