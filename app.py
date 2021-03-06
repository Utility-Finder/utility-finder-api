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

    # Fixes postgres uri deprecation in sqlalchemy
    # https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        import routes
        CORS(app)
        return app


app = create_app()

if __name__ == "__main__":
    app.run()
