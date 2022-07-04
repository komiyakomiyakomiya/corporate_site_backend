from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .mixins import Mixin


class Employee(Base, Mixin):
    __tablename__ = 'employees'

    employee_name = Column(String(64), nullable=False)
    image_path = Column(String(255), nullable=False)
    department_id = Column(Integer,
                            ForeignKey('departments.id'),
                            nullable=False)

    department = relationship('Department',
                              back_populates='employees')
    works = relationship('Work',
                         back_populates='employee')
