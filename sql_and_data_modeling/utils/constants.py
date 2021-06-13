from dotenv import dotenv_values
import psycopg2

config = dotenv_values(".env")
POSTGRES_HOST = config.get("POSTGRES_HOST")
POSTGRES_DB = config.get("POSTGRES_DB")
POSTGRES_USER = config.get("POSTGRES_USER")
POSTGRES_PASSWORD = config.get("POSTGRES_PASSWORD")
TABLE_NAME = "exercise_1"

assert (POSTGRES_HOST is not None)
assert (POSTGRES_DB is not None)
assert (POSTGRES_USER is not None)
assert (POSTGRES_PASSWORD is not None)


def get_conn(dbname=POSTGRES_DB):
    """
    Gets a database connection
    :return: cursor
    """
    conn = psycopg2.connect(dbname=dbname, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST)
    return conn, conn.cursor()
