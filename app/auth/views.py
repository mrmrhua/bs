from flask import render_template,session,redirect,request,url_for,flash
from app.auth import auth
from app.auth.form import LoginForm,RegisterForm
from app.auth.models import User
from flask.ext.login import login_required,login_user,logout_user
from .models import db
# view
@auth.route('/login',methods=['post','get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.UserName.data).first()
        if user is not None and user.verify_password(form.Passwd.data): #登陆成功
            login_user(user)
            return redirect(request.args.get('next') or url_for('auth.hello_world'))
        else:
            print('err\n');
    return render_template('auth/login.html', form=form)

@auth.route('/signin',methods=['post','get'])
def signin():
    form = RegisterForm()
    if form.validate_on_submit():  #判断数据格式-前段做
        print("1")
        user = User(username=form.Username.data,email=form.Email.data,password=form.Passwd.data)
        db.session.add(user)
        db.session.commit()
    else:
        #需要判断异常类型 >>>>>>>>>
        print('err')
    return render_template('auth/signin.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have been log out")
    redirect(url_for('auth.login'))

@auth.route('/')
@login_required
def hello_world():
   return 'Hello World!%s' % session.get('username')
