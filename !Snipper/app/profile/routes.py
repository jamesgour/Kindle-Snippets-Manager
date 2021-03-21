from app.profile import profile_bp
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Snippet

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', title='Profile')