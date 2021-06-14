from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://udacitystudios@localhost:5432/example'
db = SQLAlchemy()


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    # products = db.relationship("Product", secondary=order_items, backref=db.backref("orders", lazy=True))


class Todo(db.Model):
    """
    Create a todos table id, description, completed, and list_id, which is an index into the todos_list table
    """
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todo_lists.id"), nullable=False, default=1)

    def __repr(self):
        return f"<Todo id: {self.id}, description: {self.description}, completed: {self.completed}>"


class TodoList(db.Model):
    """
    Create a todo_list table with id, name, and a relationship with the todos table
    """
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    todos = db.relationship("Todo", backref="list", lazy=True)

    def __repr__(self):
        return f"<TodoList id: {self.id}, name: {self.name}>"
