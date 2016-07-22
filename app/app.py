# from flask import Flask
# from flask import request
# from flask import redirect
# from flask import url_for
# from flask import render_template
# from flask import jsonify
# from flask import session
# from api import api

# from models import User


# app = Flask(__name__)
# app.secret_key = 'random string'

# app.register_blueprint(api)

# # 通过 session 来获取当前登录的用户
# def current_user():
#     # print('session, debug', session.permanent)
#     username = session.get('username', '')
#     u = User.query.filter_by(username=username).first()
#     return u


# @app.route('/')
# def index():
#     view = 'index_view'
#     return redirect(url_for(view))


# # 显示登录界面的函数  GET
# @app.route('/login')
# def login_view():
#     return render_template('login.html')


# # 处理登录请求  POST
# @app.route('/login', methods=['POST'])
# def login():
#     # u = User(request.form)
#     form = request.get_json()
#     print(form)
#     username = form.get('username', '')
#     user = User.query.filter_by(username=username).first()
#     r = {
#         'success': False,
#         'message': '登录失败',
#     }
#     print(user)
#     if user is not None and user.validate_auth(form):
#         r['success'] = True
#         r['next'] = url_for('index_view')
#         session.permanent = True
#         session['username'] = username

#     else:
#         r['success'] = False
#         r['message'] = '登录失败'
#     print(r)
#     return jsonify(r)


# # 处理注册的请求  POST
# @app.route('/register', methods=['POST'])
# def register():
#     form = request.get_json()
#     u = User(form)
#     r = {
#     }
#     status, msgs = u.valid()
#     if status:
#         u.save()
#         r['success'] = True
#         # 下面这句可以在关闭浏览器后保持用户登录
#         session.permanent = True
#         session['user'] = u
#     else:
#         r['success'] = False
#         r['message'] = '\n'.join(msgs)
#     return jsonify(r)

# # 显示大厅界面的函数 GET
# @app.route('/index')
# def index_view():
#     return render_template("index.html")

    

# if __name__ == '__main__':
#     config = {
#         'debug': True,
#     }
#     app.run(**config)
