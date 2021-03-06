from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class SnippetImportForm(FlaskForm):
    source_title = StringField('Source Title')
    book_author = StringField('Author')
    snippet = StringField('Snippet', validators=[DataRequired()])
    submit = SubmitField('Submit')
