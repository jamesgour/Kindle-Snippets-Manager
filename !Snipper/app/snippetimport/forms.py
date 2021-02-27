from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class SnippetImportForm(FlaskForm):
    book_title = StringField('Book Title')
    book_author = StringField('Author')
    snippet = StringField('Snippet', validators=[DataRequired()])
    submit = SubmitField('Submit')
