import sys

from flask import Flask
from flask import render_template, request, jsonify, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import FLASK_PORT, get_conn_string
from models import db, Todo, TodoList

"""
Flask and SQLAlchemy config
"""
app = Flask(__name__, template_folder="./templates")
app.config["SQLALCHEMY_DATABASE_URI"] = get_conn_string()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return redirect(url_for("get_list_todos", list_id=1))


@app.route("/todos/lists/<list_id>/create", methods=["POST"])
def create_todo(list_id):
    error = False
    body = {}
    try:
        description = request.get_json()["description"]
        list_id = int(request.get_json()["listId"])
        todo = Todo(description=description, list_id=list_id)
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
    list_id = Todo.query.get(todo_id).list_id
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
    return render_template(
        "index.html",
        data=Todo.query.order_by("id").all(),
        active_list=list_id
    )


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=FLASK_PORT)
