from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    main_genre = db.Column(db.String)
    genre_2 = db.Column(db.String)
    genre_3 = db.Column(db.String)
    imdb_rating = db.Column(db.Float)
    length = db.Column(db.Integer)
    rank_in_year = db.Column(db.Integer)
    rating = db.Column(db.String)
    studio = db.Column(db.String)
    title = db.Column(db.String)
    worldwide_gross = db.Column(db.String)
    year = db.Column(db.Integer)
