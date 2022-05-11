from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class loginForm(FlaskForm):
    email = EmailField('Email Address',[validators.DataRequired()])
    password = PasswordField('Password',[validators.DataRequired()])
    submit = SubmitField()

class registerForm(FlaskForm):
    email = EmailField('Email Address', [validators.DataRequired()])
    password = PasswordField('Create Password',[validators.DataRequired()])
    passwordconf = PasswordField('Retype Password',[validators.DataRequired()])
    submit = SubmitField()

class fileUpload(FlaskForm):
    file = FileField()
    submit = SubmitField()