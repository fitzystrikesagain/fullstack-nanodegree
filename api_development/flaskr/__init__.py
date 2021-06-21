import os
from flask import (
    Flask,
    jsonify,
    render_template
)
from flask_cors import CORS, cross_origin
from models import setup_db, Book


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder="pages")
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route("/")
    @cross_origin()
    def hello():
        return jsonify({"message": "hello world"})

    @app.route("/books")
    def get_books():
        books = Book.query.order_by(Book.id).all()
        data = [{
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
        } for book in books]
        return jsonify(data)

    @app.route("/books/<int:book_id>")
    def get_specific_book(book_id):
        book = Book.query.get(book_id)
        data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
        }
        return jsonify(data)



    return app
