from flask import Blueprint

favorite_doctor=Blueprint('favorite_doctor',__name__,url_prefix="/user-favorite/")

from . import views