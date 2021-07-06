import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Variables(SqlAlchemyBase):
    __tablename__ = 'Variables'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    task_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("task.id", ondelete="CASCADE"))
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    range = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    task = orm.relation('Task')
