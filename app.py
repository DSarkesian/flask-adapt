"""Flask app for adopt app."""

from flask import Flask, render_template, flash, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def homepage():
    """renders homepage shows pets and availability"""
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        # flash(f"Added {name} at {price}")
        return redirect("/")
        #TODO: create flash message handling

    else:
        return render_template(
            "add.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    """show pet details and edit form"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = bool(form.available.data)

        db.session.commit()

        # flash(f"Added {name} at {price}")
        return redirect("/")
        #TODO: create flash message handling

    else:
        return render_template(
            "petInfo.html", pet=pet, form=form)


