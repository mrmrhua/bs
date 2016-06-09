from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from  flask.ext.login import LoginManager
from config import config
from flask_socketio import SocketIO
login_manager = LoginManager()
login_manager.session_protection='strong'    #安全级别较高
login_manager.login_view='auth.login'       #登陆页面的endpoint设为auth.login
db = SQLAlchemy()
socketio = SocketIO()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    from .auth import auth as auth_blueprint   #注册蓝图
    app.register_blueprint(auth_blueprint)

    from .main import  main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app