from flask import Blueprint
from flask import session
from flask import request
from flask import render_template
from flask import jsonify
from models import Tweet
from models import User

_author = 'BaiCai'

api = Blueprint('api',__name__, url_prefix='/api')

def current_user():
    # print('session, debug', session.permanent)
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u

@api.route('/tweet/add',methods=['POST'])
def tweet_add():
    r = {}
    t = Tweet(request.get_json())
    
    u = current_user()

    if u is not None and len(t.content)>0 :
        t.author_id = u.id;
        t.save()        
        r = {
            'success': True,
            'message': '发送成功',
        }
    else:
        r =  {
            'success': False,
            'message': '发送失败',
            'next': '/login',
        }
    return jsonify(r)


@api.route('/tweet/delete/<tweet_id>', methods=['POST'])
def tweet_delete(tweet_id):
    r = {}
    t = Tweet(request.get_json())

    u = current_user
    if u is not None and u.id == t.id:
        t.delete()
        r = {
            'success': True,
            'message': '删除成功'
        }
    else:
        r = {
            'success': False,
            'message': '发送失败',
            'next': '/login',
        }
    return jsonify(r)
        



