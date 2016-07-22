from flask import render_template
from flask import session
from flask import Blueprint

from ..models import User

main = Blueprint('controller', __name__)

def current_user():
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


@main.route('/')
def index_view():
    u = current_user()
    return render_template('index.html', user = u)

@main.route('/timeline')
def timeline_view():
    u = current_user()
    return render_template('timeline.html')


