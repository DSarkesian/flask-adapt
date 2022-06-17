"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, false

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet"""
    __tablename__ = "pets"

    id = db.column(db.Integer, primary_key=True, autoincrement=True)
    name = db.column(db.String, nullable=False)
    species = db.column(db.String, nullable=False)
    photo_url =db.column(db.String, nullable=False, default="")
    age = db.column(db.String,nullable=False)
    notes = db.column(db.String, nullable=True)
    available = db.column(db.Boolean, nullable=false, default =True )
