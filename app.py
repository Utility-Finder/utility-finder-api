import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

db = SQLAlchemy()

client = storage.Client()
bucket = client.get_bucket(os.environ.get('GCLOUD_BUCKET_ID'))


def create_app():
    app = Flask(__name__)

    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        import routes
        db.create_all()
        CORS(app)
        return app


app = create_app()

if __name__ == "__main__":
    app.run()
