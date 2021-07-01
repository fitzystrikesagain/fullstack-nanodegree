import logging

from flask import Flask, jsonify, request, abort
# from flask_cors import CORS, cross_origin
from flask_cors import CORS
from models import Book, setup_db

BOOKS_PER_SHELF = 8


# @TODO: General Instructions
# - As you're creating endpoints, define them and then search for TODOs
# within the frontend to update the endpoints there. If you do not update
# the endpoints, the lab will not work - of no fault of your API code!
# - Make sure for each route that you're thinking through when to abort and
# with which kind of error
# - If you change any of the response body keys, make sure you update the
# frontend to correspond.

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route("/")
    def index():
        return jsonify({
            "status": "success",
            "message": "hello world"
        })

    # TEST: When completed, the webpage will display books including title,
    # author, and rating shown as stars
    @app.route("/books")
    def get_books():
        # page = request.args.get("page", 1, default=int)
        books = Book.query.order_by(Book.id).all()
        formatted_books = [book.format() for book in books]
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * BOOKS_PER_SHELF
        end = start + BOOKS_PER_SHELF
        current_books = formatted_books[start:end]
        if len(current_books) == 0:
            abort(404)

        response = {
            "status": "success",
            "books": current_books,
            "total_books": len(formatted_books),
        }
        return jsonify(response)
        pass

    @app.route("/books/<int:book_id>", methods=["PATCH"])
    def update_rating(book_id):
        body = request.get_json()

        try:
            book = Book.query.get(book_id)
            if not book:
                abort(404)
            book.rating = body["rating"]
            book.update()

            return jsonify({
                "status": "success",
                "id": book.id
            })

        except Exception as e:
            logging.error(e)
            abort(404)

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book(book_id):
        try:
            book = Book.query.get(book_id)
            if not book:
                abort(404)
            book.delete()
            current_books = [book.format() for book in Book.query.order_by(
                Book.id).all()]

            return jsonify({
                "status": "success",
                "deleted": book.id,
                "books": current_books,
                "total_books": len(current_books),
            })

        except Exception as e:
            logging.error(e)
            abort(404)

    # @TODO: Write a route that create a new book.
    #   Response body keys: 'success', 'created'(id of created book), 'books'
    #   and 'total_books'
    # TEST: When completed, you will be able to a new book using the form.
    # Try doing so from the last page of books. Your new book should show up
    # immediately after you submit it at the end of the page.

    return app
