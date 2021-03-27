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

    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_SERVICE = os.environ.get('DB_SERVICE')
    DB_PORT = os.environ.get('DB_PORT')

    pg_uri = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVICE}:{DB_PORT}/{DB_NAME}'

    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = pg_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        import routes
        db.create_all()
        CORS(app)
        return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
