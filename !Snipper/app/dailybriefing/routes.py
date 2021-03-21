from app.dailybriefing import dailybriefing_bp
from flask import render_template
from flask_login import login_required


@dailybriefing_bp.route('/', methods=['GET'])
@dailybriefing_bp.route('/dailybriefing', methods=['GET'])
@login_required
def dailybriefing():
    #form = DailyBriefing()
    posts = [
        {
            'author': 'Mista',
            'title': 'Title A',
            'content': 'First post from Mista',
            'date_posted': 'April 20, 2017'
        },
        {
            'author': 'Mick',
            'title': 'Title B',
            'content': 'First post from Michi',
            'date_posted': 'May 30, 2020'
        }
    ]
    return render_template('dailybriefing.html', title='Daily Briefing', posts=posts)