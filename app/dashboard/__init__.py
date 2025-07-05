from flask import Blueprint

dashboard_bp = Blueprint('dashboard_bp', __name__)

from app.dashboard import route