from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    db_path = 'db.sqlite'

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'asdfsdfasdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)

    db.init_app(app)
    db.app = app

    from .api import main as api
    from .controllers import main as controllers
    from .auth import main as auth
    

    app.register_blueprint(controllers)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(auth)

    return app
