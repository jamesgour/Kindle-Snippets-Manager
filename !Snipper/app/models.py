from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    snippets = db.relationship('Snippet', backref='creator', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)

    # Password Hashing Implementation
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    

class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(90))
    source_type = db.Column(db.String(60))
    author = db.Column(db.String(60))
    snippet = db.Column(db.String(360))
    created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Snippet {}'.format(self.snippet)
 