import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class TaskSetLine(SqlAlchemyBase):
    __tablename__ = 'tasksetline'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    task_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("task.id", ondelete="CASCADE"))
    taskset_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("taskset.id", ondelete="CASCADE"))
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    task = orm.relation('TaskSet')
    users = orm.relation('Task')
