from app import db

#定义数据库表
class User(db.Model):
    __tablename__ = 'Users'
    #定义表名,省略则默认
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(32),index=True, unique= True)
    passwd = db.Column(db.String(6))
    email = db.Column(db.String(120),unique =True)

    #__repr__ 方法告诉 Python 如何打印这个类的对象。我们将用它来调试。
    def __repr__(self):
        return '<User %r>' % (self.username)