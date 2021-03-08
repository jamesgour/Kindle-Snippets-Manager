from app.snippetimport import snippetimport_bp
from flask import render_template
from app.snippetimport.forms import SnippetImportForm
from flask_login import login_required

@snippetimport_bp.route('/import', methods=['GET'])
@login_required
def snippetimport():
    form = SnippetImportForm()
    return render_template('snippetimport.html', title='Snippet Import', form=form)