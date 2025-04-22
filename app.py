from flask import Flask
from config import config
from models import db
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.blog import blog_bp_routh

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(blog_bp_routh,url_prefix='/blog')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)
