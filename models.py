from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nickname = db.Column(db.String(80),unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    def set_password(self,pwd):
        self.password = generate_password_hash(pwd)
    def check_password(self,pwd):
        return check_password_hash(self.password,pwd)
class BlogPost(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    user =db.relationship('Users',backref=db.backref('post',lazy=True))

