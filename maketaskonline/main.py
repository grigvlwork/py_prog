from flask import Flask, render_template, make_response, session
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect

from data import db_session
from data.section import Section
from data.subjects import Subjects
from data.users import User
from data.task import Task
from data.variables import Variables
from forms.user import RegisterForm, LoginForm, SubjectForm, SectionForm, TaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HSa6jK1Rb0zMDEPoTlvf5SYg4I6FtkaK'
current_email = None
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    subjects = []
    if current_user.is_authenticated:
        subjects = db_sess.query(Subjects).filter(
            (Subjects.user_id == current_user.get_id()) | (not Subjects.is_private))
    return render_template('index.html', subjects=subjects)


@app.route("/section/<subject_id>")
def section(subject_id):
    db_sess = db_session.create_session()
    subjects = []
    if current_user.is_authenticated:
        subjects = db_sess.query(Subjects).filter(
            ((Subjects.user_id == current_user.get_id()) | (not Subjects.is_private)) & (Subjects.id == subject_id))
    if subjects:
        sections = []
        sections = db_sess.query(Section).filter(Section.subject_id == subject_id)
    return render_template('section.html', sections=sections, subjects=subjects)


@app.route("/task/<subject_id>/<section_id>")
def task(subject_id, section_id):
    db_sess = db_session.create_session()
    subjects = []
    if current_user.is_authenticated:
        subjects = db_sess.query(Subjects).filter(
            ((Subjects.user_id == current_user.get_id()) | (not Subjects.is_private)) &
            (Subjects.id == subject_id))
    else:
        return redirect('index')
    if subjects:
        sections = []
        sections = db_sess.query(Section).filter((Section.subject_id == subject_id) &
                                                 (Section.id == section_id))
    else:
        return redirect('index')
    if sections:
        tasks = []
        tasks = db_sess.query(Task).filter(Task.section_id == section_id)
    else:
        return redirect('index')
    return render_template('task.html', sections=sections, subjects=subjects, tasks=tasks)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
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
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/subject_add', methods=['GET', 'POST'])
def subject_add():
    form = SubjectForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        subject = Subjects(
            name=form.name.data,
            is_private=form.is_private.data,
            user_id=current_user.get_id()
        )
        db_sess.add(subject)
        db_sess.commit()
        return redirect('/')
    return render_template('form_add.html', title='Добавление предмета', form=form)


@app.route('/section_add/<subject_id>', methods=['GET', 'POST'])
def section_add(subject_id):
    form = SectionForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        section = Section(
            name=form.name.data,
            subject_id=subject_id
        )
        db_sess.add(section)
        db_sess.commit()
        return redirect(f"/section/{subject_id}")
    return render_template('form_add.html', title='Добавление раздела', form=form)


@app.route('/task_add/<subject_id>/<section_id>', methods=['GET', 'POST'])
def task_add(subject_id, section_id):
    form = TaskForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        task = Task(
            name=form.name.data,
            section_id=section_id,
            condition=form.condition.data,
            formula=form.formula.data
        )
        db_sess.add(task)
        db_sess.commit()
        return redirect(f"/task/{subject_id}/{section_id}")
    return render_template('form_add.html', title='Добавление задачи', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)

    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


def main():
    db_session.global_init("db/maketask.sqlite")
    app.run('127.0.0.1', 8080, debug=True)


if __name__ == '__main__':
    main()
