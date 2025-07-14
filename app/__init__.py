from flask import Flask, render_template
from .extenions import db, migrate, login_manager, Toastr
from app.models.user import User
from app.models.services import Services
from app.models.menu import *

from config import  Config

def create_app(config_class = Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set your secret key

    db.init_app(app)
    migrate.init_app(app,db)
    Toastr.init_app(app)  # Initialize Flask-Toastr
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'  # Set the login view for Flask-Login

    # Ensure the database is created
    @login_manager.user_loader
    def load_user(user_id):
            return User.query.get(int(user_id))

    # Register blueprint here
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    from app.incident import incident_bp
    app.register_blueprint(incident_bp, url_prefix='/incident')

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return {
            'message': 'This is the contact page. You can reach us at '
        }
   

    with app.app_context():
            db.create_all()

            if Services.query.count() == 0:
                    db.session.add(Services(name='Application Support', description='Application support team',vendor='Tecnotree Nigeria', sla=5))
                    db.session.add(Services(name='Developer Team', description='Dev team',vendor='CWG company', sla=5))
                    db.session.add(Services(name='Email delivery', description='Windows team',vendor='Techmandira Limited', sla=2.5))
                    db.session.add(Services(name='Cloud services', description='cloud team ',vendor='Tavia Technology', sla=5))
                    db.session.add(Services(name='Asset Management', description='asset managers',vendor='Techmandira Limited', sla=5))
                    db.session.add(Services(name='Cleaning', description='cleaner manager',vendor='Availago Global', sla=5))
                    db.session.commit()

    return app

