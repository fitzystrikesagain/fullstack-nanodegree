import os

FLASK_PORT = os.environ.get("FLASK_PORT")


def get_conn_string():
    postgres_user = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    postgres_host = os.environ.get("POSTGRES_CONTAINER_NAME", "postgres-fsnd")
    postgres_db = os.environ.get("POSTGRES_DB", "todoapp")

    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
