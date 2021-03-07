from app.authentication import authentication_bp
from flask import render_template, flash, redirect
from app.authentication.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    # In case already logged-in user accidentally navigates to /login
    if current_user.is_authenticated:
        return redirect(url_for('dailybriefing.dailybriefing'))
    form = LoginForm()

    # If form is submitted, check db if user info is correct then flash error or log user in
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('authentication.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dailybriefing.dailybriefing'))
    
    # Display login page - previous block is skipped when page first loads
    return render_template('login.html', title='Login', form=form)


@authentication_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))