from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import Mixin
from database import Base


class WorkTag(Base, Mixin):
    __tablename__ = 'works_tags'

    work_id = Column(Integer,
                    ForeignKey('works.id'))
    tag_id = Column(Integer,
                    ForeignKey('tags.id'))

    # work = relationship('Work',
    #                      back_populates='tags')
    # tag = relationship('Tag',
    #                 back_populates='works')
