from . import db
from . import ReprMixin

import time


class User(db.Model, ReprMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    created_time = db.Column(db.Integer)

    tweets = db.relationship('Tweet', backref='user')

    @staticmethod  
    def user_by_name(username):
        return User.query.filter_by(username=username).first() 

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = int(time.time())

    def json(self):
        self.id 
        d = {k:v for k,v in self.__dict__.items() if k not in self.blacklist()   }
        return d
    
    def blacklist(self):
        b = [
            '_sa_instance_state',
            'password'
        ]
        return b
        
    def validate_auth(self, form):
        username = form.get('username', '')
        password = form.get('password', '')
        username_equals = self.username == username
        password_equals = self.password == password
        print('validate auth', username, password, username_equals, password_equals)
        return username_equals and password_equals
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def register_validate(self):
        min_len = 3
        valid_username = User.query.filter_by(username=self.username).first() == None
        valid_username_len = len(self.username) >= min_len
        valid_password_len = len(self.password) >= min_len
        msgs = []
        if not valid_username_len:
            message = '用户名长度必须大于3'
            msgs.append(message)
        elif not valid_password_len:
            message = '密码长度必须大于3'
            msgs.append(message)
        elif not valid_username:
            message = '用户已经存在'
            msgs.append(message)
           
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs



