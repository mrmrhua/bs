from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin
from app import login_manager
#定义数据库表
class User(UserMixin,db.Model):
    __tablename__ = 'Users'
    #定义表名,省略则默认
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(32),index=True, unique= True,nullable=False)
    #passwd = db.Column(db.String(6))
    passwd_hash = db.Column(db.String(128),nullable=False)

    @property
    def password(self):     #把该方法变成属性
        raise AttributeError('password unreadable')  #提示不可读

    @password.setter  #上面那个属性的setter方法
    def password(self,password):
        self.passwd_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.passwd_hash,password)

    email = db.Column(db.String(120), unique=True, index=True)
    Nickname = db.Column(db.String(12))

    #__repr__ 方法告诉 Python 如何打印这个类的对象。我们将用它来调试。
    def __repr__(self):
        return '<User %r>' % (self.username)
