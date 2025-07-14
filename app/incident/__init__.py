from flask import Blueprint

incident_bp = Blueprint('incident_bp',__name__)

from app.incident import route