from ..models import User
from ..models import Tweet

from . import main
from . import current_user

from flask import request
from flask import jsonify


@main.route('/tweet/add',methods=['POST'])
def tweet_add():
    u = current_user()
    r = {}
    t = Tweet(request.get_json())
    t.user = u   

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


@main.route('/tweet/delete/<tweet_id>', methods=['POST'])
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
        