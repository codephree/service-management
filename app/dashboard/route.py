from flask import redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from app.dashboard import dashboard_bp

@dashboard_bp.route('/')
@login_required
def index():
    if not current_user.is_authenticated:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth_bp.login'))
   
    return render_template('dashboard/index.html', user=current_user)

@dashboard_bp.route('/settings')
@login_required
def settings():
    if not current_user.is_authenticated:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth_bp.login'))
    
    # Here you would typically fetch user settings from the database
    # For now, we will just render a placeholder template
    return render_template('dashboard/settings.html')
    
    
