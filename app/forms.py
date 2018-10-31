from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	# DataRequired验证器只是简单的检查相应域提交的数据是否为空
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)