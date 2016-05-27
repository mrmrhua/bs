from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from  flask.ext.login import LoginManager
from config import config

login_manager = LoginManager()
login_manager.session_protection='strong'    #安全级别较高
login_manager.login_view='auth.login'       #登陆页面的endpoint设为auth.login
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app