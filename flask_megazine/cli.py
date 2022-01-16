import click
from flask import Flask
from flask.cli import AppGroup
from .models import User

app = Flask(__name__)
user_cli = AppGroup('user')

@user_cli.command('create')
@click.argument('username')
@click.argument('password')
@click.option('--display_name', type=click.STRING)
def create_user(username, password, display_name=None):
    user = User(username=username, display_name=display_name)
    user.set_password(password)
    user.save()


def init_cli(app):
    app.cli.add_command(user_cli)
