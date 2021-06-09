"""
Lesson 4 Exercise 2
"""
from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
fake = Faker()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User ID: {self.id}, name: {self.name}>"


q1 = "\n#1. Implement a query to filter all users by name 'Bob'."
print(q1)
bob_query = User.query.filter(User.name == "Bob")
print(bob_query.all())

q2 = "\n#2. Implement a LIKE query to filter the users for records with a name that includes the letter 'b'"
print(q2)
query = User.query.filter(User.name.like("B%"))
print('query = User.query.filter(User.name.like("B%"))')

q3 = "\n#3. Return only the first 5 records of the query above."
print(q3)
for row in query.limit(5).all():
    print(row)

q4 = "\n#4. Re-implement the LIKE query using case-insensitive search."
print(q4)
query = User.query.filter(User.name.ilike("B%"))
for user in query.all():
    print(user.name)

q5 = "\n#5. Return the number of records of users with name 'Bob'."
print(q5)
number_of_bobs = User.query.filter(User.name == "Bob").count()
verb = "is" if number_of_bobs == 1 else "are"
print(f"There {verb} {number_of_bobs} records with the name Bob")
