from flask_wtf import Form
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	yzm = StringField('yzm', validators=[DataRequired()])
	submit = SubmitField('submit')