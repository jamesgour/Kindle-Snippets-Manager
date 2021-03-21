from flask import Blueprint

snippetlibrary_bp = Blueprint(
    'snippetlibrary', __name__, 
    template_folder='templates'
)

from app.snippetlibrary import routes