import unittest
from flask import current_app, jsonify
from app import create_app
from app.models import db


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_app_exists(self):
        self.assertFalse(current_app is None, msg=None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'], msg=None)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == '__main__':
    unittest.main()
