import json
import unittest

from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, db_uri, Book


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = db_uri
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        books = Book.query.filter(Book.title == 'Anansi Boys')
        for book in books:
            book.delete()
        """Executed after reach test"""
        pass

    # @TODO: Write at least two tests for each endpoint - one each for success
    #   and error behavior. You can feel free to write additional tests for
    #   nuanced functionality, Such as adding a book without a rating, etc.
    #   Since there are four routes currently, you should have at least eight
    #   tests.
    #   Optional: Update the book information in setUp to make the test database
    #   your own!

    """
    @app.route('/books')
    """

    def test_book_endpoint(self):
        """
        Tests to see whather the /books endpoint returns a 200 to a GET
        :return: boolean
        """
        res = self.client().get('/books')
        self.assertEqual(res.status_code, 200)

    def test_books_exist(self):
        """
        Ensures the list of books returned by /books is not None or emtpy
        :return:
        """
        res = self.client().get('/books')
        books = res.get_json().get("books")
        self.assertTrue(books)
        self.assertTrue(len(books) > 0)

    """
    @app.route('/books', methods=['POST'])
    """

    def test_create_new_book(self):
        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['books']))

    """
    @app.route('/books/<int:book_id>', methods=['PATCH'])
    """
    """
    @app.route('/books/<int:book_id>', methods=['DELETE'])
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
