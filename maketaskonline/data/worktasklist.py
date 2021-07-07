import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Worktasklist(SqlAlchemyBase):
    __tablename__ = 'worktasklist'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"))
    task_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("task.id", ondelete="CASCADE"))
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    task = orm.relation('Task')
    users = orm.relation('User')
