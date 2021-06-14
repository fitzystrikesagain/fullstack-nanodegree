import sys

from flask import render_template, request, jsonify, redirect, url_for

from config import create_app, create_db, FLASK_PORT
from models import Todo, TodoList


"""
Flask and SQLAlchemy config
"""
app = create_app()
db, migrate = create_db()
db.init_app(app)


@app.route("/")
def index():
    return redirect(url_for("get_list_todos", list_id=1))


@app.route("/todos/create", methods=["POST"])
def create_todo():
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
