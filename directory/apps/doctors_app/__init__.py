from flask import Blueprint


doctors=Blueprint('doctors',__name__,url_prefix='/user-doctors/')

from . import views