from app.auth import auth_bp
from app.extenions import db
from app.models.user import User
from app.forms import LoginForm, RegisterForm, ResetPasswordForm
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info') 
        return redirect(url_for('dashboard_bp.index'))  # Redirect to dashboard if already logged in
    
    # If the user is not authenticated, proceed with login  
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remeber = form.remember_me.data
        # print(email, password, remeber)
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Logic for successful login (e.g., setting session)
            login_user(user, remember=remeber)  # Use the remember parameter to set the session cookie
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard_bp.index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return render_template('auth/login.html', form=form)
        
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info') 
        return redirect(url_for('dashboard_bp.index'))  # Redirect to dashboard if already logged in
    
    # If the user is not authenticated, proceed with login  
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()   
        if existing_user:
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('auth_bp.login'))

        # Here you would typically create a new user instance and save it to the database
        new_user = User(name=name, email=email, password=generate_password_hash(password, method='scrypt'))  # Assuming User model has these fields
        # Assuming you have a session or database to add the new user   
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth_bp.login'))  # Redirect to login page after successful registration

        # Logic for user registration
        return render_template('auth/register.html', form=form)     

    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()   
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/recover', methods=['GET', 'POST'])
def recover():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info') 
        return redirect(url_for('dashboard_bp.index'))
    # If the user is not authenticated, proceed with password recovery  
    form = ResetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            # Logic to send password reset email
            flash('A password reset link has been sent to your email.', 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash('Email not found. Please check your email or register.', 'danger')
            return render_template('auth/recover.html', form=form)
    return render_template('auth/recover.html',form=form) 

@auth_bp.route('/reset')
def reset():    
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info') 
        return redirect(url_for('dashboard_bp.index'))
    return render_template('auth/reset.html')   
