import os
from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not test_config:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    @app.route("/")
    def hello():
        return jsonify({"message": "HELLO WORLD"})

    @app.route("/smiley")
    def smiley():
        return ":)"

    return app
