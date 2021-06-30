from flask import Flask, render_template, make_response, session
from werkzeug.utils import redirect

from data import db_session
from data.users import User
from forms.user import RegisterForm, HeaderLoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HSa6jK1Rb0zMDEPoTlvf5SYg4I6FtkaK'
current_email = None


@app.route("/index", methods=['GET', 'POST'])
def index():
    # visits_count = session.get('visits_count', 0)
    # session['visits_count'] = visits_count + 1
    # return make_response(
    #     f"Вы пришли на эту страницу {visits_count + 1} раз")
    form = HeaderLoginForm()
    if form.validate_on_submit():
        if form.submit_login.data:
            return redirect('/login')
        if form.submit_register.data:
            current_email = form.email.data
            return redirect('/register')
    return render_template('unlogged.html', title='Вход', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if current_email:
        form.email_default = current_email
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run('127.0.0.1', 8080, debug=True)


if __name__ == '__main__':
    main()
