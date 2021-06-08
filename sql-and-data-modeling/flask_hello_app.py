import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

FLASK_PORT = os.environ.get("FLASK_PORT")

app = Flask(__name__)
uri = "postgresql://postgres:postgres@postgres-fsnd:5432/mydb"
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

"""
Exercise 4

    Run the script, so that the persons table exists.
    Run the application, with debug mode on.
    Create a person record in the persons table, by connecting to psql and using INSERT INTO.
    Change the index route from saying "Hello World!" to saying "Hello" to the name of a person in the persons table.
    Preview the app in the browser, and see it output "Hello" next to the name of the person record in the database.
"""


class Person(db.Model):
    """
    Exercise 3

    Create a SQLALchemy model, Person, with custom table name persons, that includes ID and name attributes, in the
    server script app.py. Have SQLAlchemy create the persons table if it doesn't exist already, whenever the server is
    run. Run the server. In the terminal, check that SQLAlchemy ORM successfully created the table by connecting to the
    database using psql.
    """
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<Person ID: {self.id}, name: {self.name}>"


db.create_all()


@app.route("/")
def index():
    person = Person.query.filter(Person.id == 2).first()
    return f"Hello {person.name}!"


@app.route('/person/<id>')
def get_and_greet_person(id):
    """
    Exercise 4

        Run the script, so that the persons table exists.
        Run the application, with debug mode on.
        Create a person record in the persons table, by connecting to psql and using INSERT INTO.
        Change the index route from saying "Hello World!" to saying "Hello" to the name of a person in the persons table.
        Preview the app in the browser, and see it output "Hello" next to the name of the person record in the database.
    """

    person = Person.query.filter(Person.id == id).first()
    if not person:
        return "Person not found"
    return f"Hello {person.name}!"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=FLASK_PORT)
