import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'task'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    section_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("section.id", ondelete="CASCADE"))
    condition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    formula = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    section = orm.relation('Section')
