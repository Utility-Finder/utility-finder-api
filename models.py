from . import db


class Utility(db.Model):
    id = db.Column(db.String(80), primary_key=True)  # TODO: change this
    type = db.Column(db.Integer(), nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    lon = db.Column(db.Float(), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
