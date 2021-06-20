import sys

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from sqlalchemy import desc

from config import FLASK_PORT, get_conn_string
from models import db, Movie

"""
Flask and SQLAlchemy config
"""

app = Flask(__name__, template_folder="flaskr/pages")
app.config["SQLALCHEMY_DATABASE_URI"] = get_conn_string()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    top_ten = "movies/top_ten"
    data = {"top_ten": top_ten}
    return render_template("hello.html",
                           title="Movies",
                           message="Welcome to the Movies site",
                           data=data)


@app.route("/movies/<int:movie_id>")
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    movie_title = movie.title
    data = {
        "studio": movie.studio,
        "gross": movie.worldwide_gross,
        "year": movie.year,
        "length": movie.length,
        "rating": movie.rating,
    }
    return render_template("movie_page.html", movie_title=movie_title, data=data)


@app.route("/movies/top_ten")
def get_top_ten():
    movies = Movie.query.order_by(desc(Movie.worldwide_gross)).limit(10).all()
    top_ten = [{
        "id": m.id,
        "title": m.title,
        "gross": m.worldwide_gross
    } for m in movies]
    # top_ten = [[m.title, m.worldwide_gross] for m in movies]

    return render_template("top_ten.html", title="Top ten movies", top_ten=top_ten)


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=FLASK_PORT)
