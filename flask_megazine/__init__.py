from flask import Flask
from .config import get_config
from .models import init_db
from .cli import init_cli
from .blueprints.admin.auth import init_login_manager
from .blueprints.admin import admin_bp
from .blueprints.main import main_bp

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)

    config = get_config(config_name)
    app.config.from_object(config)

    init_db(app)
    init_cli(app)
    init_login_manager(app)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(main_bp, url_prefix='/')

    return app
