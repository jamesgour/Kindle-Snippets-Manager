from flask import Blueprint

snippetimport_bp = Blueprint(
    'snippetimport', __name__, 
    template_folder='templates'
)

from app.snippetimport import routes