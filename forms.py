"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL",
                        validators=[Optional(), URL()])
    age = StringField("Age")
    notes = TextAreaField("Notes")