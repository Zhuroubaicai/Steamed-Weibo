from app from init_app
from app import models

def rebuild_db():
    app = init_app()
    db = models.db
    db.drop_all()
    db.create_all()
    print('auth rebuild database')


def run():
    config = dict{
        debug = True,
    }