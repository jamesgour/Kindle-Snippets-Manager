from app.dailybriefing import dailybriefing_bp
from flask import render_template
from flask_login import login_required


@dailybriefing_bp.route('/', methods=['GET'])
@dailybriefing_bp.route('/dailybriefing', methods=['GET'])
@login_required
def dailybriefing():
    return render_template('dailybriefing.html', title='Daily Briefing')