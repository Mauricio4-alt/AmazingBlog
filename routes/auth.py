from flask import Blueprint,request,jsonify
from models import Users,db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    nickname = data.get('nickname')
    password = data.get('password')
    if Users.query.filter_by(nickname=nickname).first():
        return jsonify({'msg':'Username already exists'}),409
    user = Users(nickname=nickname)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
@auth_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    nickname = data.get('nickname')
    password = data.get('password')
    user = Users.query.filter_by(nickname=nickname).first()

    if user and user.check_password(password):
        token = create_access_token(identity=user.id)
        return jsonify({"token":token}),200
    else:
        return jsonify({'msg':'Invalid Credentials'}),401
