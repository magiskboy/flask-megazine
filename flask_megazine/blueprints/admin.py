from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, static_url_path='/admin/static')

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')
