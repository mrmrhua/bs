
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

#定义网页表单
class LoginForm(Form):
    UserName = StringField('登 录', validators=[DataRequired()])
    Passwd = PasswordField('密 码')
    SubmitBtn = SubmitField('>')