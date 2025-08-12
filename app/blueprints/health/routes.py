from flask import Blueprint, render_template, request, jsonify
from .models import HealthArticle

health_bp = Blueprint('health', __name__, template_folder='../../templates/health')

@health_bp.route('/tools')
def tools():
    # mock symptom checker interface
    articles = HealthArticle.query.limit(20).all()
    return render_template('tools.html', articles=articles)
