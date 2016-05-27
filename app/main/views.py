from flask import render_template,session
from . import main
from .form import LoginForm
from .models import User

# view
@main.route('/login',methods=['post','get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.UserName.data).first()
        if user is not None and user.passwd == form.Passwd.data: #登陆成功
            # session['username'] = form.UserName.data
            print('1\n');
        else:
            print('err\n');
    return render_template('login.html', form=form)


@main.route('/')
def hello_world():

   return 'Hello World!%s' % session.get('username')
