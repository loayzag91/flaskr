from . import api
from app.models import Entries
from flask import jsonify


@api.route('/posts/', methods=['GET'])
def get_all():
    posts = Entries.query.all()
    return jsonify({ 'posts': [post.to_json() for post in posts] })


@api.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Entries.query.get_or_404(id)
    return jsonify(post.to_json())
