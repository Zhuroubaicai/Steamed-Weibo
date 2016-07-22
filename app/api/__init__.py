from flask import Blueprint
from flask import session
from flask import request
from flask import render_template
from flask import jsonify
from ..models import Tweet
from ..models import User

_author = 'BaiCai'

main = Blueprint('api',__name__)

def current_user():
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u

def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if current_user() is None:
            r = {
                'success': False,
                'message': '未登录',
            }
            return jsonify(r)
        return f(*args, **kwargs)
    return function

from . import tweet