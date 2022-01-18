import sqlalchemy as sa
from ._config import db, ModelMixin


class Post(db.Model):
    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(200), nullable=False, index=True)
    content = sa.Column(sa.String(5000), nullable=False)
    slug = sa.Column(sa.String(300), nullable=False)
    category_id = sa.Column(sa.Integer(), sa.ForeignKey('category.id'), nullable=False)
    created_by_id = sa.Column(sa.Integer(), sa.ForeignKey('user.id'), nullable=False)
    updated_by_id = sa.Column(sa.Integer(), sa.ForeignKey('user.id'))
    created_at = sa.Column(sa.DateTime(), default=sa.sql.func.now())
    updated_at = sa.Column(sa.DateTime(), onupdate=sa.sql.func.now())

    category = sa.orm.relationship('Category', backref='posts')
    author = sa.orm.relationship('User', lazy='joined', backref='posts', primaryjoin='User.id == Post.created_by_id')
