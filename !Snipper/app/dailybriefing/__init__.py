from flask import Blueprint

dailybriefing_bp = Blueprint(
    'dailybriefing', __name__, 
    template_folder='templates'
)

from app.dailybriefing import routes