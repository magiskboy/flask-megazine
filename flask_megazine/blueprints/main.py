from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, static_url_path='/static')

@main_bp.route('/')
def index():
    return render_template('main/index.html')
