"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species",
         validators= [InputRequired(), AnyOf(["dog","cat","porcupine"])])
    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])
    age = StringField("Age",
        validators= [InputRequired(), AnyOf(["baby", "young", "adult", "senior"])])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pet info."""

    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField(label='available')