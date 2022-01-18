from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class ModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
