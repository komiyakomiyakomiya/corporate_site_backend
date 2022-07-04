from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import Mixin
from database import Base


class Work(Base, Mixin):
    __tablename__ = 'works'

    image_path = Column(String(255), nullable=False)
    employee_id = Column(Integer,
                        ForeignKey('employees.id'),
                        nullable=False)

    employee = relationship('Employee',
                            back_populates='works')
    tags = relationship('Tag',
                        secondary='works_tags',
                        back_populates='works')
