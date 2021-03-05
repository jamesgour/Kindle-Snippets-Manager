from app.authentication import authentication_bp
from flask import render_template, flash, redirect
from app.authentication.forms import LoginForm

@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/dailybriefing')
    return render_template('login.html', title='Login', form=form)