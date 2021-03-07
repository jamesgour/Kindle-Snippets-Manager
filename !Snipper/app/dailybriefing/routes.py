from app.dailybriefing import dailybriefing_bp
from flask import render_template


@dailybriefing_bp.route('/', methods=['GET'])
@dailybriefing_bp.route('/dailybriefing', methods=['GET'])
@login_required
def dailybriefing():
    #form = DailyBriefing()
    return render_template('dailybriefing.html', title='Daily Briefing')