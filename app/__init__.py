from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(testing=False):

    app = Flask(__name__)

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "sqlite:///:memory:"
        )
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "sqlite:///app.db"
        )

    app.config["TESTING"] = testing
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import api

    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app
