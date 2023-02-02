from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length


class AddPetForm(FlaskForm):
    """ Form for adding Pet """
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Please Enter a Name")])

    species = SelectField("Pet Species", validators=[
                          InputRequired(message="Please Enter a Species")], choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine"), ("other", "Other")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Pet age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Age must be between 0 - 30")])

    notes = StringField("Pet Notes", validators=[Optional(),  Length(max=50)])


class EditPetForm(FlaskForm):
    """ Form for editing an existing Pet """
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Pet age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Age must be between 0 - 30")])

    notes = StringField("Pet Notes", validators=[Optional(),  Length(max=50)])

    available = BooleanField("Available?")
