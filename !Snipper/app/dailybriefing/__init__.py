from flask import Blueprint

bp = Blueprint('dailybriefing', __name__)

from app.main import routes