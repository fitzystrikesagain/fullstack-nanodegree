import os
import sys

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

FLASK_PORT = os.environ.get("FLASK_PORT")
app = Flask(__name__, template_folder="./templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@postgres-fsnd:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    """
    Create a todos table with dolumns id and description
    """
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)

    def __repr(self):
        return f"<Todo id: {self.id}, description: {self.description}>"


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
        return jsonify({
            "description": todo.description
        })
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)


@app.route("/")
def index():
    return render_template("index.html", data=Todo.query.all())


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=FLASK_PORT)
