from flask import Blueprint


doctors=Blueprint('doctors',__name__,url_prefix='/doctors/')

from . import views