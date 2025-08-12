import os
from flask import Flask
from .extensions import db, migrate
from .config import Config
from .services import firebase as firebase_service

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    env = os.getenv('FLASK_ENV', 'production')
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # initialize firebase (if credentials provided)
    firebase_service.init_app(app)

    # register blueprints
    from .blueprints.auth.routes import auth_bp
    from .blueprints.community.routes import community_bp
    from .blueprints.digital_literacy.routes import dl_bp
    from .blueprints.health.routes import health_bp
    from .blueprints.wellness.routes import wellness_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(community_bp, url_prefix='/community')
    app.register_blueprint(dl_bp, url_prefix='/courses')
    app.register_blueprint(health_bp, url_prefix='/health')
    app.register_blueprint(wellness_bp, url_prefix='/wellness')

    # simple index route
    @app.route('/')
    def index():
        from .models.user import User
        # sample dynamic content for index template
        sample_courses = [{'id':1,'title':'Computer Basics'},{'id':2,'title':'Internet Safety'}]
        return app.render_template('index.html', user=None, courses=sample_courses)

    return app
