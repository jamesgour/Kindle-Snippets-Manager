from app.snippetimport import snippetimport_bp
from flask import render_template

@snippetimport_bp.route('/import', methods=['GET'])
def snippetimport():
    #form = DailyBriefing()
    return render_template('snippetimport.html', title='Snippet Import')