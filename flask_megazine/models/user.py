import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from ._config import db, ModelMixin


class User(db.Model, ModelMixin):
    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(20), unique=True, index=True, nullable=False)
    password_hash = sa.Column(sa.String(128), nullable=False)
    display_name = sa.Column(sa.String(50), nullable=False, unique=True)
    profile_url = sa.Column(sa.String(200), nullable=True)
    created_at = sa.Column(sa.DateTime(True), default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(True), onupdate=sa.func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
