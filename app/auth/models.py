from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin
import datetime
from app import login_manager
#定义数据库表



class Relationship(db.Model):
    __tablename__ = 'Relationship'
    re_id = db.Column(db.Integer,primary_key=True)
    friend_a = db.Column(db.Integer,db.ForeignKey('User.id'))
    friend_b = db.Column(db.Integer,db.ForeignKey('User.id'))


class User(UserMixin,db.Model):
    __tablename__ = 'User'
    #定义表名,省略则默认
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(32),index=True, unique= True,nullable=False)
    #passwd = db.Column(db.String(6))
    passwd_hash = db.Column(db.String(128),nullable=False)

    email = db.Column(db.String(120), unique=True, index=True)
    Nickname = db.Column(db.String(12),default='无名')

    @property
    def password(self):  # 把该方法变成属性
        raise AttributeError('password unreadable')  # 提示不可读

    @password.setter  # 上面那个属性的setter方法
    def password(self, password):
        self.passwd_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    mygroup = db.relationship('ns_table',backref='owner',lazy='dynamic') # group.owner指回对应的User
                                                                        # dynamic 使user.mygroup属性可以用QUERY语句
    def addgroup(self,gname):   #增加一个某名字的组
       if self.mygroup.filter_by(group_name = gname).first() is None:   #没有重名
            g = ns_table(group_name = gname,user_id=self.get_id())
            db.session.add(g)
            return True
       else:
           return False

    myrelation1 = db.relationship('Relationship',foreign_keys=[Relationship.friend_a] \
                                    ,lazy= 'dynamic')
    myrelation2 = db.relationship('Relationship', foreign_keys=[Relationship.friend_b] \
                                  , lazy='dynamic')


    def makefriends(self,user):
        if not self.are_friends(user):
            r = Relationship(friend_a = self.get_id(),friend_b = user.id)
            db.session.add(r)
            return True
        else:
            return False

    def are_friends(self,user):   #已经是朋友,返回True
         return self.myrelation.filter_by(friend_b = user.id).first() is not None \
                 or \
                self.myrelation2.filter_by(friend_a = user.id).first() is not None

    def sendmessage(self,to,cont):
        m = Message(from_id = self.get_id(),to_id = to.get_id(),content = cont,send_time=datetime.datetime.now() )
        db.session.add(m)
        return True

    mybelong = db.relationship('gu_table',backref=db.backref('who',lazy='joined'),lazy='dynamic')
    #__repr__ 方法告诉 Python 如何打印这个类的对象。我们将用它来调试。
    def __repr__(self):
        return '<User %r>' % (self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Message(db.Model):
    __tablename__ = 'Messages'
    message_id = db.Column(db.Integer,primary_key=True)
    from_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    to_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    content = db.Column(db.Text,nullable=False)
    send_time = db.Column(db.DateTime)

class ns_table(db.Model):
    __tablename__ = 'ns_table'
    ns_id = db.Column(db.Integer,primary_key=True)
    group_name = db.Column(db.String(32))
    group_size = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    member = db.relationship('gu_table', lazy='dynamic')

    def addtogroup(self,user):
        if self.member.filter_by(user_id=user.id).first() is None:
            gu = gu_table(ns_id=self.ns_id,user_id=user.id)
            db.session.add(gu)
            self.group_size += 1
            db.session.add(self)
            return True
        else:
            return False



class gu_table(db.Model):
    __tablename__ = 'gu_table'
    gu_id = db.Column(db.Integer,primary_key=True)
    ns_id = db.Column(db.Integer,db.ForeignKey('ns_table.ns_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'))
#连接到User取名字
