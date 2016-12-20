from flask import Flask, render_template


def create_app(app):
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')

    from app.models import db
    db.init_app(app)
    with app.app_context():
	# Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()


    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

