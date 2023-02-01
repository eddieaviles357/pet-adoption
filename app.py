# flask --debug run

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI="postgresql:///pet_adoption",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
    SECRET_KEY="mensajesecreto",
    DEBUG_TB_INTERCEPT_REDIRECTS=False
)
# Debug Extension on
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    """ Home page """
    return render_template("index.html")
