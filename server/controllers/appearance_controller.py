from flask import  request, jsonify
from flask.views import MethodView
from server.extensions import db
from server.models.appearance import Appearance

class AppearanceController(MethodView):
    def post(self):
        data = request.get_json()
        try:
            appearance = Appearance(
                rating=data['rating'],
                guest_id=data["guest_id"],
                episode_id=data["episode_id"]
            )
            # rating validation
            if not (1 <= appearance.rating <= 5):
                return jsonify({"error": "Rating must be between 1 and 5"}), 400

            db.session.add(appearance)
            db.session.commit()
            return jsonify(appearance.to_dict()), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400