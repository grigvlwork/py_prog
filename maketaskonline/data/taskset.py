import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class TaskSet(SqlAlchemyBase):
    __tablename__ = 'taskset'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"))
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    users = orm.relation('User')
