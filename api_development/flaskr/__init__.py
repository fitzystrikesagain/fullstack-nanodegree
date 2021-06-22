from flask import (
    Flask,
    jsonify,
    request,
)
from flask_cors import CORS, cross_origin
from models import setup_db, Book

PAGINATION_INCREMENT = 10


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
                template_folder="pages")
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods",
                             "GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route("/")
    @cross_origin()
    def hello():
        return jsonify({"message": "hello world"})

    @app.route("/books", methods=["GET", "POST"])
    def get_books():
        books = Book.query.order_by(Book.id).all()
        page = request.args.get("page", 1, type=int)
        formatted_books = [book.format() for book in books]
        start = (page - 1) * PAGINATION_INCREMENT
        end = start + PAGINATION_INCREMENT
        response = {
            "meta": 200,
            "data": formatted_books[start:end],
            "total_books": len(formatted_books),
        }
        return jsonify(response)

    @app.route("/books/<int:book_id>")
    def get_specific_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify(
                {
                    "meta": 404,
                    "data": "Not found"
                }
            )
        return jsonify(
            {
                "meta": 200,
                "data": book.format()
            }
        )

    return app
