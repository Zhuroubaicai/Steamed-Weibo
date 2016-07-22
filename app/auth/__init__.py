from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask import redirect

from ..models import User


main = Blueprint('auth', __name__)

def current_user():
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


@main.route('/login')
def login_view():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    username = form.get('username', '') 
    user = User.user_by_name(username)

    r = {
        'success': False,
        'message': '登录失败',
    }

    #验证用户名和密码
    if user is not None and user.validate_auth(form):
        r['success'] = True
        r['next'] = request.args.get('next',url_for('controller.index_view'))
        session.permanent = True
        session['username'] = username
    return jsonify(r)

@main.route('/register', methods=['POST'])
def register():
    form = request.get_json()
    u = User(form)
    r = {
        'success': True,
    }
    status,msgs = u.register_validate()
    if status:
        u.save()
        r['success'] = True
        r['next'] = request.args.get('next', url_for('controller.index_view'))
        session.permanent = True
        session['username'] = u.username
    else:
        r['success'] = False
        r['message'] = '\n'.join(msgs)
    return jsonify(r) 

@main.route('/logout')
def logout():
    session['username'] = None
    return render_template('index.html', user=None)

