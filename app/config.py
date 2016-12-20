import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY= 'development key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    USERNAME='admin'
    PASSWORD='default'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flaskr.db')

