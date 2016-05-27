
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo,Email
from .models import User

#定义网页表单
class LoginForm(Form):
    UserName = StringField('登 录', validators=[DataRequired()])
    Passwd = PasswordField('密 码',validators=[DataRequired()])
    SubmitBtn = SubmitField('>')

class RegisterForm(Form):
    Username = StringField('用 户 名', validators=[DataRequired()])
    Passwd = PasswordField('密 码',validators=[DataRequired(),EqualTo('Passwdrepeat',message='两次输入的密码不一致')])
    Passwdrepeat = PasswordField('确 认 密 码',validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(),Email()])

    SubmitBtn = SubmitField('>')

    def unique_email(self,field):
        if User.query.filter(email=field.data).first():
            raise ValidationError('email exits already')

    def unique_username(self, field):
        if User.query.filter(username = field.data).first():
            raise ValidationError('email exits already')