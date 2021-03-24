from flask import Blueprint

comment=Blueprint('comment',__name__,url_prefix='/comment/')

from . import views