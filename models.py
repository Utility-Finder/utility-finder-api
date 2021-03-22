import uuid
from sqlalchemy.dialects.postgresql import UUID
from . import db


class Utility(db.Model):
    """Utility model
    """
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = db.Column(db.Integer(), nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    lon = db.Column(db.Float(), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
