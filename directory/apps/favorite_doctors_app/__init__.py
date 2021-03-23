from flask import Blueprint

favorite_doctor=Blueprint('favorite_doctor',__name__,url_prefix="/favorite/")

from . import views