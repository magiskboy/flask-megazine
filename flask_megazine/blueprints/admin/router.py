import os
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from .form import LoginForm, UpdateProfileForm
from .auth import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin_bp.route('/posts', methods=['GET'])
@login_required
def posts():
    return 'post'


@admin_bp.route('/users', methods=['GET'])
@login_required
def users():
    return 'users'


@admin_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    template = 'admin/profile.html'
    method = request.method
    

    if method == 'GET':
        form = UpdateProfileForm(obj=current_user)
        return render_template(template, form=form)

    form = UpdateProfileForm()
    if not form.validate_on_submit():
        for _, message in form.errors.items():
            flash(message, 'danger')
    else:
        try:
            if form.profile.data:
                file = form.profile.data
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    'flask_megazine',
                    'static', 
                    'admin',
                    'profiles',
                    filename
                ))
                current_user.profile_url = url_for('static', filename=f'admin/profiles/{filename}')

            current_user.username = form.username.data
            current_user.display_name = form.display_name.data
            current_user.password = form.password.data
            current_user.save()
        except SQLAlchemyError:
            flash('Occur error when update profile', 'danger')
            return redirect(url_for('admin.profile'))

        flash('Profile was updated', 'success')
    return redirect(url_for('admin.profile'))


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))

    template = 'admin/login.html'
    login_form = LoginForm()
    method = request.method
    ctx = {
        'title': 'Login',
        'form': login_form
    }

    if method == 'GET':
        return render_template(template, **ctx)

    if not login_form.validate_on_submit():
        for _, message in login_form.errors.items():
            flash(message, 'danger')
        return redirect(url_for('admin.login'))

    user = User.query.filter_by(username=login_form.username.data).first()
    if (not user) or (not user.verify_password(login_form.password.data)):
        flash('User not found', 'danger')
        return redirect(url_for('admin.login'))

    # login with flask-login
    login_user(user, login_form.remember.data)
    flash(f'Hi, {user.display_name}', 'success')
    return redirect(url_for('admin.index'))


@admin_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
