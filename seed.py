from app import create_app
from app.extensions import db
from app.models.user import User
from app.blueprints.digital_literacy.models import Course, Lesson
from app.blueprints.health.models import HealthArticle
from app.blueprints.community.models import Post
from app.blueprints.wellness.models import SupportResource

app = create_app()
with app.app_context():
    db.create_all()
    if not User.query.first():
        u = User(email='admin@example.com', name='Admin', is_admin=True)
        u.set_password('password')
        db.session.add(u)
    if not Course.query.first():
        c1 = Course(title='Computer Basics', description='Learn to use a computer.')
        c2 = Course(title='Internet Safety', description='Stay safe online.')
        db.session.add_all([c1, c2])
    if not HealthArticle.query.first():
        a = HealthArticle(title='Handwashing 101', content='Wash hands regularly.', verified=True)
        db.session.add(a)
    if not Post.query.first():
        p = Post(user_id=1, title='Welcome', body='Welcome to the community!')
        db.session.add(p)
    if not SupportResource.query.first():
        r = SupportResource(title='Mental Health Hotline', link='tel:0800111234', description='24/7 support')
        db.session.add(r)
    db.session.commit()
    print('Seed data created.')
