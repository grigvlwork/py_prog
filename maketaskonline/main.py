import re

from flask import Flask, render_template, make_response, session, request, url_for
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data import db_session
from data.section import Section
from data.subjects import Subjects
from data.users import User
from data.task import Task
from data.variables import Variables
from data.worktasklist import Worktasklist
from data.taskset import TaskSet
from data.tasksetline import TaskSetLine
from forms.user import RegisterForm, LoginForm, SubjectForm, SectionForm, TaskForm, VariablesForm, ToWorkForm, \
    TaskListForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HSa6jK1Rb0zMDEPoTlvf5SYg4I6FtkaK'
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


# Проверка доступности объекта текущему пользователю
def available(object, object_id):
    db_sess = db_session.create_session()
    if object == "subjects":
        subjects = db_sess.query(Subjects).filter(Subjects.id == object_id).one()
        if not subjects:
            return False
        if subjects.user_id == int(current_user.get_id()):
            return True
    elif object == "section":
        section = db_sess.query(Section).filter(Section.id == object_id).one()
        if section:
            return available('subjects', section.subject_id)
    elif object == "task":
        task = db_sess.query(Task).filter(Task.id == object_id).one()
        if task:
            return available('section', task.section_id)
    elif object == "variables":
        variable = db_sess.query(Variables).filter(Variables.id == object_id).one()
        if variable:
            return available('task', variable.task_id)
    return False


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


@app.route("/worktasklist", methods=['GET', 'POST'])
@login_required
def worktasklist():
    db_sess = db_session.create_session()
    worktask = db_sess.query(Worktasklist).filter(Worktasklist.user_id == current_user.get_id()).all()
    print(worktask[0].task.name)
    form = TaskListForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        worktasklist = db_sess.query(Worktasklist).filter(Worktasklist.user_id == current_user.get_id())
        for task in worktasklist:
            tl = TaskSetLine(
                task_id=task.task_id,
                user_id=task.user_id,
                amount=task.amount
            )
            db_sess.add(tl)
        worktasklist = db_sess.query(Worktasklist).filter(Worktasklist.user_id == current_user.get_id()).all()
        db_sess.delete(worktasklist)
        db_sess.commit()
        return redirect(url_for('tasklist'))
    return render_template('worktasklist.html', worktask=worktask, form=form)

@app.route("/delworktask/<worktask_id>")
@login_required
def delworktask(worktask_id):
    db_sess = db_session.create_session()
    worktask = db_sess.query(Worktasklist).filter(Worktasklist.id == worktask_id).one()
    db_sess.delete(worktask)
    db_sess.commit()
    return redirect(url_for("worktasklist"))


@app.route("/section/<subject_id>")
@login_required
def section(subject_id):
    if not available("subjects", subject_id):
        return redirect("index")
    db_sess = db_session.create_session()
    subject = db_sess.query(Subjects).filter(Subjects.id == subject_id).one()
    sections = db_sess.query(Section).filter(Section.subject_id == subject_id)
    return render_template('section.html', sections=sections, subject=subject)


@app.route("/task/<subject_id>/<section_id>")
@login_required
def task(subject_id, section_id):
    if not(available("subjects", subject_id) and available("section", section_id)):
        return redirect("index")
    db_sess = db_session.create_session()
    subject = db_sess.query(Subjects).filter(Subjects.id == subject_id).one()
    section = db_sess.query(Section).filter(Section.id == section_id).one()
    tasks = db_sess.query(Task).filter(Task.section_id == section_id)
    return render_template('task.html', section=section, subject=subject, tasks=tasks)


@app.route("/variables/<subject_id>/<section_id>/<task_id>", methods=['GET', 'POST'])
@login_required
def variables(subject_id, section_id, task_id):
    if not(available("subjects", subject_id) and
           available("section", section_id) and (available("task", task_id))):
        return redirect("index")
    db_sess = db_session.create_session()
    subject = db_sess.query(Subjects).filter(Subjects.id == subject_id).one()
    section = db_sess.query(Section).filter(Section.id == section_id).one()
    task = db_sess.query(Task).filter(Task.id == task_id).one()
    variables = db_sess.query(Variables).filter(Variables.task_id == task_id).all()
    if not variables:
        vars = sorted(list(set(re.findall(r"\{(.*?)\}", task.condition))))
        db_sess = db_session.create_session()
        for var in vars:
            variable = Variables(
                name=var,
                task_id=task.id,
                type="",
                range=""
            )
            db_sess.add(variable)
        db_sess.commit()
    variables = db_sess.query(Variables).filter(Variables.task_id == task_id)
    form = ToWorkForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        wortasklist = Worktasklist(
            task_id=task_id,
            user_id=current_user.get_id(),
            amount=form.amount.data
        )
        db_sess.add(wortasklist)
        db_sess.commit()
        return redirect(url_for('worktasklist'))

    return render_template('variables.html', section=section, subject=subject, task=task,
                           variables=variables, form=form)


@app.route("/edit_var/<subject_id>/<section_id>/<task_id>/<var_id>", methods=["GET", "POST"])
@login_required
def edit_var(subject_id, section_id, task_id, var_id):
    if not(available("subjects", subject_id) and available("section", section_id) and
           (available("task", task_id)) and available("variables", var_id)):
        return redirect("index")
    form = VariablesForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        var = db_sess.query(Variables).filter(Variables.id == var_id).one()
        if var:
            form.type.data = var.type
            form.range.data = var.range
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        var = db_sess.query(Variables).filter(Variables.id == var_id).one()
        if var:
            var.type = form.type.data
            var.range = form.range.data
            db_sess.commit()
            return redirect(url_for('variables', subject_id=subject_id, section_id=section_id, task_id=task_id))
            # return render_template('variables.html', section=section, subject=subject, task=task, variables=variables)
        else:
            abort(404)
    return render_template('edit_var.html', title="Редактирование переменной", form=form, var=var)


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


@login_required
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
@login_required
def section_add(subject_id):
    if not available("subjects", subject_id):
        return redirect("index")
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
@login_required
def task_add(subject_id, section_id):
    if not(available("subjects", subject_id) and available("section", section_id)):
        return redirect("index")
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


def main():
    db_session.global_init("db/maketask.sqlite")
    app.run('127.0.0.1', 8080, debug=True)


if __name__ == '__main__':
    main()
