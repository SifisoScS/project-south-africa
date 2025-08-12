from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from ...extensions import db
from ...models.user import User
from .forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('Logged in (mock)', 'success')
            return redirect(url_for('community.feed'))
        flash('Invalid credentials', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash('Email already registered', 'warning')
            return render_template('auth/login.html', form=form)
        user = User(email=form.email.data, name=form.name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully (mock)', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)
