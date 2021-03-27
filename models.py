import os
import uuid
from google.cloud.storage import bucket
from sqlalchemy.dialects.postgresql import UUID
from . import db


class Utility(db.Model):
    """Utility model
    """
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = db.Column(db.Integer(), nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    lon = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_json(self):
        bucket_name = os.environ.get('GCLOUD_BUCKET_ID')
        image_url = f'http://storage.googleapis.com/{bucket_name}/static/{self.id}.png'
        return {
            'id': self.id,
            'type': self.type,
            'lat': self.lat,
            'lon': self.lon,
            'imageURL': image_url,
            'description': self.description,
            'rating': 0,  # TODO: calculate rating
        }
