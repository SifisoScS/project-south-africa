from flask import Blueprint, render_template
from .models import SupportResource

wellness_bp = Blueprint('wellness', __name__, template_folder='../../templates/wellness')

@wellness_bp.route('/support')
def support():
    resources = SupportResource.query.limit(20).all()
    return render_template('support.html', resources=resources)
