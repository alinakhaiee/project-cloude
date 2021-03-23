from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from directory.config import Config
from flask_jwt_extended import JWTManager
app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
jwt_manager=JWTManager(app)


@app.route('/')
def index():
    return{"massege":"wolcome to flask-app"}

from directory.apps.users_app import users
app.register_blueprint(users)
from directory.apps.favorite_doctors_app import favorite_doctor
app.register_blueprint(favorite_doctor)