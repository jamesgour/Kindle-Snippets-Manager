from flask import Blueprint

profile_bp = Blueprint(
    'profile', __name__, 
    template_folder='templates'
)

from app.profile import routes