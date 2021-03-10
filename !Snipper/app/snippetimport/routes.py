from app.snippetimport import snippetimport_bp
from flask import render_template
from app.snippetimport.forms import SnippetImportForm
from flask_login import login_required

@snippetimport_bp.route('/import', methods=['GET', 'POST'])
@login_required
def snippetimport():
    form = SnippetImportForm()

# If form is submitted, add new data to db and commit the session
    if form.validate_on_submit():
        source_title = Snippet(source_title=form.source_title.data)
        book_author = 
        snippet = 
        user_id = 

        # From login data > using for reference
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered!')
        return redirect(url_for('authentication.login'))
    return render_template('snippetimport.html', title='Snippet Import', form=form)