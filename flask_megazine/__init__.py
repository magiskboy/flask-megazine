from flask import Flask
from .blueprints.admin import admin_bp
from .blueprints.main import main_bp

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(main_bp, url_prefix='/')

    return app
