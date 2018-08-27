# _*_ encoding:utf-8 _*_
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = 'xiao'
__date__ = '2018/8/23 10:44'


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message="长度不符合规定")])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message="page区间非法")], default=1)
