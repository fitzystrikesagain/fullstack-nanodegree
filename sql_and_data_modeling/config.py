import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

FLASK_PORT = os.environ.get("FLASK_PORT")


def create_app():
    app = Flask(__name__, template_folder="./templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = get_conn_string()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    return app


def create_db():
    app = create_app()
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return db, migrate


def get_conn_string():
    postgres_user = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    postgres_host = os.environ.get("POSTGRES_CONTAINER_NAME", "postgres-fsnd")
    postgres_db = os.environ.get("POSTGRES_DB", "todoapp")

    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
