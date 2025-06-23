from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from server.config import Config
from server.controllers.guest_controller import GuestController
from server.extensions import db


migrate=Migrate()
jwt=JWTManager()

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    with app.app_context():
        from server.models import guest 

    guest_view = GuestController.as_view('guest_api')
    app.add_url_rule('/guests/', defaults={'id': None}, view_func=guest_view, methods=['GET', 'POST'])
    app.add_url_rule('/guests/<int:id>', view_func=guest_view, methods=['GET', 'DELETE'])


    return app
