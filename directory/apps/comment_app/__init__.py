from flask import Blueprint

comment=Blueprint('comment',__name__,url_prefix='/user-comment/')

from . import views