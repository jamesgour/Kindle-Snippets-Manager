from app.snippetlibrary import snippetlibrary_bp
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Snippet

@snippetlibrary_bp.route('/snippetlibrary', methods=['GET', 'POST'])
@login_required
def snippetlibrary():
    posts = [
        {
            'author': 'Mista',
            'title': 'Title A',
            'content': 'First post from Mista',
            'date_posted': 'April 20, 2017'
        },
        {
            'author': 'Mick',
            'title': 'Title B',
            'content': 'First post from Michi',
            'date_posted': 'May 30, 2020'
        }
    ]
    return render_template('snippetlibrary.html', title='Snippet Library', posts=posts)