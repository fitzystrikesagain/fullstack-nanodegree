from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

order_items = db.Table(
    "order_items",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True)
)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    products = db.relationship("Product", secondary=order_items, backref=db.backref("orders", lazy=True))


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


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
