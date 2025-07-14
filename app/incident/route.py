from app.incident import incident_bp
from flask import render_template
from app.models.menu import *


@incident_bp.route('/')
def index():
    context = {
        'incident': Incident.query.all(),
        'title': 'Your Incident',
        'description': 'Manage your incident here',
        'active_page': 'incident'
    }


    return render_template('incident/index.html', context=context)


