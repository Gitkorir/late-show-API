from flask import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
migrate=Migrate()
jwt=JWTManager()

def create_app():
    app= Flask(__name__)
    app.config.form_object(config)

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    return app
