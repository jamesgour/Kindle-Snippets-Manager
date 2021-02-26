from flask import Blueprint

bp = Blueprint('dailybriefing', __name__, template_folder='templates')

from app.dailybriefing import routes