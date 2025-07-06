from flask import Flask, render_template
from .extenions import db, migrate, login_manager, Toastr
from app.models.user import User

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

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

   
    return app

