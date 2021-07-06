import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Section(SqlAlchemyBase):
    __tablename__ = 'section'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    subject_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("subjects.id", ondelete="CASCADE"))
    subject = orm.relation('Subjects')
