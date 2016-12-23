import unittest
from flask import current_app, jsonify
from app import create_app
from app.models import db


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.tester = current_app.test_client()
        db.create_all()

    def login(self, username, password):
        return self.tester.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.tester.get('/logout', follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_api_null_call(self):
       rv = self.tester.get('/api/v1.0/posts/')
       assert b'"posts": []' in rv.data

    def test_api_call(self):
        self.login('admin', 'default')
        rv = self.tester.post('/add', data=dict(
            title='Hello',
            text='Testing fields'
        ), follow_redirects=True)
        rv = self.tester.get('/api/v1.0/posts/')
        assert b'"posts": []' not in rv.data
        assert b'"posts": [\n    {\n' in rv.data
        assert b'"id": 1, \n' in rv.data
        assert b'"text": "Testing fields", \n' in rv.data
        assert b'"title": "Hello"\n    }\n  ]' in rv.data

    def test_api_id_call(self):
        self.login('admin', 'default')
        rv = self.tester.post('/add', data=dict(
            title='Hello',
            text='Testing fields'
        ), follow_redirects=True)
        rv = self.tester.get('/api/v1.0/posts/1')
        assert b'"id": 1,' in rv.data
        assert b'"text": "Testing fields",' in rv.data
        assert b'"title": "Hello"' in rv.data

if __name__ == '__main__':
    unittest.main()
