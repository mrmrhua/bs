from flask_socketio import SocketIO,emit
from manage import socketio

print("test\n")
@socketio.on('connect')
def test_conn():
    emit('my response',{'data':'have connected'})

@socketio.on('message')
def rece_mes(msg):
    print(msg)