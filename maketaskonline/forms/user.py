from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired


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


class SectionForm(FlaskForm):
    name = StringField('Название раздела', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class TaskForm(FlaskForm):
    name = StringField('Название задачи', validators=[DataRequired()])
    condition = TextAreaField('Условие задачи', validators=[DataRequired()])
    formula = TextAreaField('Формула для вычисления ответа', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class VariablesForm(FlaskForm):
    # name = StringField('Название переменной', validators=[DataRequired()])
    type = RadioField('Тип переменной', choices=['Число', 'Текст'], validators=[DataRequired()])
    range = TextAreaField('Диапазон изменения значений', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class ToWorkForm(FlaskForm):
    # name = StringField('Название переменной', validators=[DataRequired()])
    amount = IntegerField('Количество задач', validators=[DataRequired()])
    submit = SubmitField('Добавить задачи в работу')


class TaskListForm(FlaskForm):
    name = StringField('Название работы', validators=[DataRequired()])
    submit = SubmitField('Сформировать работу')


class VariantsForm(FlaskForm):
    amount = IntegerField('Количество вариантов в работе', validators=[DataRequired()])
    submit = SubmitField('Сформировать файл')