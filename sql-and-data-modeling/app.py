import os

from flask import Flask, request

app = Flask(__name__)

FLASK_PORT = os.environ.get("FLASK_PORT")


@app.route("/")
def index():
    s = "Hello!"
    return s


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=FLASK_PORT)
