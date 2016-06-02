from ..auth.models import User
from app.main import main
from flask import render_template
from flask.ext.login import login_required
from flask.ext.login import current_user

@login_required
@main.route("/dash",methods=['post','get'])
def dash():
    if current_user.is_authenticated:   #current_user是一个User类
        user = User.query.filter_by(username=current_user.username).first()
        # print(user.ickname)
        return render_template("main/DASH.html",user=user)
