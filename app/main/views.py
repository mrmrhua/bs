from ..auth.models import User
from app.main import main
from flask import render_template
from flask.ext.login import login_required
from flask.ext.login import current_user
from app import socketio
from flask_socketio import SocketIO,emit
# from manage import socketio
@login_required
@main.route("/dash",methods=['post','get'])
def dash():
    if current_user.is_authenticated:   #current_user是一个User类
        user = User.query.filter_by(username=current_user.username).first()
        # print(user.ickname)
        return render_template("main/DASH.html",user=user)


@socketio.on('connect')
def test_conn():
    emit('my response',{'data':'have connected'})

@socketio.on('message')
def rece_mes(message):
    print(message)