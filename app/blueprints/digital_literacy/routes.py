from flask import Blueprint, render_template, jsonify
from .models import Course, Lesson

dl_bp = Blueprint('digital_literacy', __name__, template_folder='../../templates/digital_literacy')

@dl_bp.route('/')
def list_courses():
    courses = Course.query.limit(50).all()
    # simple JSON endpoint + template
    return render_template('course.html', courses=courses)
