from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from server.config import Config
from server.controllers.guest_controller import GuestController
from server.extensions import db
from server.controllers.episode_controller import EpisodeController
from server.controllers.appearance_controller import AppearanceController
from server.models.user import User
from server.controllers.auth_controller import AuthController

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

    episode_view = EpisodeController.as_view('episode_api')
    app.add_url_rule('/episodes/', defaults={'id': None}, view_func=episode_view, methods=['GET', 'POST'])
    app.add_url_rule('/episodes/<int:id>', view_func=episode_view, methods=['GET', 'DELETE'])

    appearance_view = AppearanceController.as_view('appearance_api')
    app.add_url_rule('/appearances/', view_func=appearance_view, methods=['POST'])

    auth_view = AuthController.as_view('auth_api')
    app.add_url_rule('/register', defaults={'action': 'register'}, view_func=auth_view, methods=['POST'])
    app.add_url_rule('/login', defaults={'action': 'login'}, view_func=auth_view, methods=['POST'])





    return app
