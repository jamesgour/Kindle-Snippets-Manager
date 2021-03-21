from app.snippetlibrary import snippetlibrary_bp
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import User, Snippet

@snippetlibrary_bp.route('/snippetlibrary', methods=['GET', 'POST'])
@login_required
def snippetlibrary():
    snippets = current_user.own_snippets()
    return render_template('snippetlibrary.html', title='Snippet Library', snippets=snippets)