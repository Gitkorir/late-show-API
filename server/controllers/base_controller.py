from flask import request, jsonify
from server.extensions import db
from flask.views import MethodView
from werkzeug.exceptions import NotFound

class BaseController(MethodView):

    model = None  # To be set in child class

    def get(self, id=None):
        if id is None:
            records = self.model.query.all()
            return jsonify([r.to_dict() for r in records]), 200
        else:
            record = self.model.query.get(id)
            if not record:
                raise NotFound(f"{self.model.__name__} with ID {id} not found.")
            return jsonify(record.to_dict()), 200

    def delete(self, id):
        record = self.model.query.get(id)
        if not record:
            raise NotFound(f"{self.model.__name__} with ID {id} not found.")
        db.session.delete(record)
        db.session.commit()
        return '', 204  # No content

    def post(self):
        try:
            data = request.get_json()
            instance = self.model(**data)
            db.session.add(instance)
            db.session.commit()
            return jsonify(instance.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
