from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app:SQLAlchemy):
    """
    Instantiates the database as it relates to the application.
    Creates all models as tables within the postgres db

    Args:
        app (SQLAlchemy): the SQLAlchemy app
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
