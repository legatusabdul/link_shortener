from flask import Flask
from flask_sqlalchemy import SQLAlchemy

CONNECTION_STRING: str = "postgresql://user:admin@127.0.0.1:54320/user"

ORM_DATABASE = None


def init_db(app: Flask):
    global ORM_DATABASE

    app.config["SQLALCHEMY_DATABASE_URI"] = CONNECTION_STRING
    app.config["SECRET_KEY"] = "sUpeRSecr3t!Str1ng" # encrypt user cookies, use Environment Variable

    ORM_DATABASE = SQLAlchemy(app)

    # do not remove imports, they are used implicitly
    from models.db import UrlDBModel

    with app.app_context():
        ORM_DATABASE.create_all()
