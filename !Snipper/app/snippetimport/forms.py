from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired

class SnippetImportForm(FlaskForm):
    snippet = TextAreaField('Snippet', validators=[DataRequired()])
    source = StringField('Source')
    author = StringField('Author')
    source_type_choices = [('book', 'Book'), ('mag', 'Magazine'), ('person','Person')] 
    source_type = SelectField('Source Type', choices=source_type_choices)
    submit = SubmitField('Submit')
