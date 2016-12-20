from flask import Flask, render_template
from app.config import conlist


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(conlist[config_name])

    from app.models import db
    db.init_app(app)
    with app.app_context():
	# Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()


    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

