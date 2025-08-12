from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models.user import User
from .models import Post

community_bp = Blueprint('community', __name__, template_folder='../../templates/community')

@community_bp.route('/feed')
def feed():
    posts = Post.query.order_by(Post.created_at.desc()).limit(20).all()
    return render_template('feed.html', posts=posts)
