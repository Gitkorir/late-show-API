from flask import request, jsonify
from flask.views import MethodView
from server.extensions import db
from server.models.user import User
from flask_jwt_extended import create_access_token

class AuthController(MethodView):
    def post(self, action):
        data = request.get_json()

        if action == 'register':
            if not data.get('username') or not data.get('password'):
                return jsonify({"error": "Username and password are required"}), 400

            if User.query.filter_by(username=data['username']).first():
                return jsonify({"error": "Username already exists"}), 400

            user = User(username=data['username'])
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201

        elif action == 'login':
            user = User.query.filter_by(username=data.get('username')).first()
            if user and user.check_password(data.get('password')):
                token = create_access_token(identity=user.id)
                return jsonify({ "access_token": token }), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"error": "Invalid action"}), 400
