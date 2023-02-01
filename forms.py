from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """ Form for adding Pet """
    name = StringField("Pet Name", validators=[
                       InputRequired("Please Enter a Name")])
    species = StringField("Pet Species")
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Pet age", validators=[Optional()])
    notes = StringField("Pet Notes", validators=[Optional()])
