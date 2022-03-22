from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField(label="Email: ", validators=[DataRequired(), Email()])
    password = PasswordField(label="PassWord: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")