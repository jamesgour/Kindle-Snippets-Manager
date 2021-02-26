from app.dailybriefing import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/dailybriefing', methods=['GET', 'POST'])
def dailybriefing():
    #form = DailyBriefing()
    return render_template('dailybriefing.html', title='Daily Briefing')