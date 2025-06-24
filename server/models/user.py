from server.extensions import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    password_harsh=db.Column(db.String(200), nullable=False)