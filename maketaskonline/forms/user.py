from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Регистрация')


class HeaderLoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    submit_login = SubmitField('Вход')
    submit_register = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class SubjectForm(FlaskForm):
    name = StringField('Название предмета', validators=[DataRequired()])
    is_private = BooleanField('Доступен только мне')
    submit = SubmitField('Сохранить')
