import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Variants(SqlAlchemyBase):
    __tablename__ = 'variants'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    taskset_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("taskset.id", ondelete="CASCADE"))
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    answers = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    file = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    taskset = orm.relation('TaskSet')
