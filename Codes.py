from flask import Flask,render_template,redirect,url_for,session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

sqluser = 'Coder'
sqlpw = '123456'
sqlhost = 'localhost'
sqldb = 'bs'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello ding'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://'+ sqluser + ":" +\
    sqlpw + "@" + sqlhost + "/" + sqldb

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

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


#定义网页表单
class LoginForm(Form):
    UserName = StringField('login', validators=[DataRequired()])
    Passwd = PasswordField('pw')
    SubmitBtn = SubmitField('submit')


# view
@app.route('/login',methods=['post','get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.UserName.data).first()
        if user.passwd == form.Passwd.data: #登陆成功
        #session['username'] = form.UserName.data

            return redirect(url_for('hello_world'))
        else:
            return "passwd error"
    return render_template('login.html', form=form)

@app.route('/')
def hello_world():
    return 'Hello World!%s' % session.get('username')


if __name__ == '__main__':
    app.run(debug=True)
