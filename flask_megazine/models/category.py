import sqlalchemy as sa
from ._config import db, ModelMixin


class Category(db.Model):
    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(50), nullable=False, index=True)
    description = sa.Column(sa.String(200))
    slug = sa.Column(sa.String(100), nullable=False)
    created_at = sa.Column(sa.DateTime(), default=sa.sql.func.now())
