import email
from wsgiref.validate import validator
from wtforms import StringField,PasswordField,SubmitField,EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,length,EqualTo
from flask_sqlalchemy import SQLAlchemy

class Login(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('SignUp')
class Signup(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validator=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    conferm = PasswordField('Confirmer_Password',validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('SignUp')
