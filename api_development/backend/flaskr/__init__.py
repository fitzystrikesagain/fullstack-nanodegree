from flask import Flask, jsonify, request, abort
# from flask_cors import CORS, cross_origin
from flask_cors import cross_origin, CORS

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
    @cross_origin()
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

    # @TODO: Write a route that will update a single book's rating.
    #   It should only be able to update the rating, not the entire
    #   representation and should follow API design principles regarding
    #   method and route.
    #   Response body keys: 'success'
    # TEST: When completed, you will be able to click on stars to update a
    # book's rating and it will persist after refresh
    @app.route("/books/<int:book_id>")
    @cross_origin()
    def get_specific_book(book_id):
        return jsonify({
            "id": book_id
        })
        pass

    # @TODO: Write a route that will delete a single book.
    #   Response body keys: 'success', 'deleted'(id of deleted book), 'books'
    #   and 'total_books'
    #   Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, you will be able to delete a single book by
    # clicking on the trashcan.

    # @TODO: Write a route that create a new book.
    #   Response body keys: 'success', 'created'(id of created book), 'books'
    #   and 'total_books'
    # TEST: When completed, you will be able to a new book using the form.
    # Try doing so from the last page of books. Your new book should show up
    # immediately after you submit it at the end of the page.

    return app
