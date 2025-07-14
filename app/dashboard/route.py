from flask import redirect, url_for, flash, render_template, jsonify, request
from flask_login import login_required, current_user
from app.forms import SettingsForm
from app.dashboard import dashboard_bp
from app.models.user import User
from app.extenions import db


@dashboard_bp.route('/')
@login_required
def index():   
    return render_template('dashboard/index.html', user=current_user)

@dashboard_bp.route('/settings', methods=['GET','POST'])
@login_required
def settings():
    
    user = User.query.get_or_404(current_user.id)
    
    form = SettingsForm()
    form.name.data = user.name
    
    context = {
        'form': form,
        'user': current_user,
        'title': 'Settings',    
        'description': 'Manage your account settings',
        'active_page': 'settings'
    }
    
    if form.validate_on_submit():
        print(request.form.get("name"))
       
        user.name = request.form.get("name")
        db.session.commit()

        flash({'title':'Successful','message': 'Your settings have been updated.'}, 'success')
        # return redirect(url_for('dashboard_bp.settings'))
        return render_template('dashboard/settings.html', context=context)
    
    
    return render_template('dashboard/settings.html', context=context)
    