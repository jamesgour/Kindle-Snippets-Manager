from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    snippets = db.relationship('Snippet', backref='user', lazy=True)

    def __repr__(self):
        """Clean representation of User class"""
        return f"User('{self.username}', '{self.email}')"

    # Password hashing implementation
    def set_password(self, password):
        """Converts a password string into a secure password hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies whether a password string is equal to its password hash"""
        return check_password_hash(self.password_hash, password)

    # Snipper Functions
    def own_snippets(self):
        """Return current user's own snippets in descending order"""
        own = Snippet.query.filter_by(user_id=self.id)
        desc_own = own.order_by(Snippet.created_dtm.desc())
        return desc_own

@login.user_loader
def load_user(id):
    return User.query.get(int(id))  

class Snippet(db.Model):
    __tablename__ = 'snippet'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(90), nullable=False)
    source_type = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String(60))
    snippet = db.Column(db.String(360), nullable=False)
    created_dtm = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Clean representation of Snippet class"""
        return f"Snippet('{self.source}', '{self.snippet}')"
 