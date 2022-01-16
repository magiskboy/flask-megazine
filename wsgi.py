import os
from flask_megazine import create_app

FLASK_ENV = os.getenv('FLASK_ENV')

app = create_app(FLASK_ENV)
