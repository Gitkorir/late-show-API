from server.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    password_harsh=db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_harsh= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_harsh,password)  

    def to_dict(self):
        return {
            'id':self.id,
            'username':self.username
        }  