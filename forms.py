from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):
    """ Form for adding Pet """
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Please Enter a Name")])

    species = SelectField("Pet Species", validators=[
                          InputRequired(message="Please Enter a Species")], choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine"), ("other", "other")])

    photo_url = StringField("Photo URL", validators=[Optional()])

    age = IntegerField("Pet age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Age must be between 0 - 30")])

    notes = StringField("Pet Notes", validators=[Optional()])
