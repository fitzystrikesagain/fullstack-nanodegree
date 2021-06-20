import os

from flask_sqlalchemy import SQLAlchemy

FLASK_PORT = os.environ.get("FLASK_PORT")
db = SQLAlchemy()


def get_conn_string():
    postgres_user = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    postgres_host = os.environ.get("POSTGRES_CONTAINER_NAME", "postgres")
    postgres_db = os.environ.get("POSTGRES_DB", "movies")

    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
