from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    snippets = db.relationship('Snippet', backref='creator', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)

class Snippet(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   source_title = db.Column(db.String(90))
   author = db.Column(db.String(60))
   snippet = db.Column(db.String(360))
   created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   def __repr__(self):
       return 'Snippet {}'.format(self.snippet)

