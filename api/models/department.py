from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import Mixin
from database import Base


class Department(Base, Mixin):
    __tablename__ = 'departments'

    department_name = Column(String(50), nullable=False)

    employees = relationship('Employee',
                            back_populates='department')
