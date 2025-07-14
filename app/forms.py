from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember_me = BooleanField('Remember Me')  # Optional field for remember me functionality {{ url_for('auth.login') }} {{ url_for('auth.register') }}
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')    

class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordConfirmForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])  
    submit = SubmitField('Reset Password')

class SettingsForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=3, max=25)])
    # username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    # password = PasswordField('Old Password', validators=[DataRequired(), Length(min=6)])
    # new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)]) 
    submit = SubmitField('Update Settings')

    def validate_username(self, username):
        # Add custom validation logic if needed
        pass

    def validate_email(self, email):
        # Add custom validation logic if needed
        pass   
    
     
class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

    def validate_current_password(self, current_password):
        # Add custom validation logic if needed
        pass    