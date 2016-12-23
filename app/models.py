from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Entries(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(140), nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '{},{}'.format(self.title, self.text)

    def to_json(self):
        json_post = {
            'id': self.id,
            'title': self.title,
            'text': self.text
        }
        return json_post
