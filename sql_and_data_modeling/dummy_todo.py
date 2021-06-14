import os
import sys

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""
Postgres config
"""
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.environ.get("POSTGRES_CONTAINER_NAME", "postgres-fsnd")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "todoapp")
FLASK_PORT = os.environ.get("FLASK_PORT")

"""
Flask and SQLAlchemy config
"""
app = Flask(__name__, template_folder="./templates")
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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


@app.route("/")
def index():
    return redirect(url_for("get_list_todos", list_id=1))


@app.route("/todos/create", methods=["POST"])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()["description"]
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body["description"] = todo.description
    except Exception as e:
        print(e)
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)


@app.route("/lists/<int:list_id>")
def get_list_todos(list_id):
    return render_template(
        template_name_or_list="index.html",
        lists=TodoList.query.all(),
        todos=Todo.query.filter_by(list_id=list_id).order_by("id").all(),
        active_list=TodoList.query.get(list_id)
    )


@app.route("/todos/<todo_id>/set-completed", methods=["POST"])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()["completed"]
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


@app.route("/todos/<todo_id>/delete", methods=["DELETE"])
def delete_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
    return render_template("index.html", data=Todo.query.order_by("id").all())


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=FLASK_PORT)
