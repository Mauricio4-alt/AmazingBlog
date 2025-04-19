from datetime import timedelta
import configparser 
class config:
    SECRET_KEY = 'superSecretKey'
    SQLALCHEMY_DATABASE_URI ='postgres+psycopg2://postgres:mauricioj18@localhost/amazinblog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JWT_SECRET_KEY = 'paralelepipedo'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
