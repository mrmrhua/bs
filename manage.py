#启动脚本

#!/usr/bin/env python
from app import create_app,db
from app.auth.models import User
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand
from flask_socketio import SocketIO,emit
app =create_app('default')
manager = Manager(app)
# socketio = SocketIO(app)
#def make_shell_context():
   # return dict(app=app,db=db)
#manager.add_command("shell", Shell(make_context=make_shell_context()))
# Shell()启动一个Python shell。可以传进去一个make_context参数，这个参数必须是一个字典。
# 相当于引入很多包
# @socketio.on('connect')
# def test_conn():
#     emit('my response',{'data':'have connected'})
#
# @socketio.on('message')
# def rece_mes(msg):
#     print(msg)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)  #add_commnd自定义SHELL指令,对应到相应的function

if __name__=='__main__':
       # app.run()
    # socketio.run(app)
     manager.run()