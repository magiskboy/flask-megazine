from flask_wtf import FlaskForm
from wtforms import fields, validators


class LoginForm(FlaskForm):
    username = fields.StringField(label='Username', validators=[validators.InputRequired(), validators.Length(4, 20)])
    password = fields.PasswordField(label='Password', validators=[validators.InputRequired(), validators.Length(8, 16)])
    remember = fields.BooleanField("Remember me?", default=False)


class UpdateProfileForm(FlaskForm):
    username = fields.StringField(label='Username', validators=[validators.Length(4, 20)])
    password = fields.PasswordField(label='Password', validators=[validators.Length(8, 16)])
    display_name = fields.StringField(label='Display name')
    profile = fields.FileField(label='Profile')
