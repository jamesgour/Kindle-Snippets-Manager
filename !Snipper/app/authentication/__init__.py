from flask import Blueprint

authentication_bp = Blueprint(
    'authentication', __name__, 
    template_folder='templates'
)

from app.authentication import routes