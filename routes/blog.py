from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from models import BlogPost,db, Users

blog_bp_routh = Blueprint('blog',__name__)

@blog_bp_routh.route('/post',methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = get_jwt_identity()
    if not title or not content:
        return jsonify({'msg':'Title and content required'}),400
    
    post =BlogPost(title=title,content=content,user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'msg':'Post created succefull'}),201


@blog_bp_routh.route('/post')
def get_post():
    posts = BlogPost.query.all()
    results = []
    for post in posts:
        results.append({
            'title':post.title,
            'content':post.content,
            'user_id':post.user_id
        })
    return jsonify(results),200