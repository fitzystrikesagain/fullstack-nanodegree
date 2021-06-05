import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

with open(os.path.expanduser('~/.pgpass'), 'r') as f:
    host, port, database, user, password = f.read().split(':')

# Connect to the database
SQLALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{host}/{database}"
