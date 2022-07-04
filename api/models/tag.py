from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import Mixin
from database import Base


class Tag(Base, Mixin):
    __tablename__ = 'tags'

    tag_name = Column(String(50), nullable=False)

    works = relationship('Work',
                        secondary='works_tags',
                        back_populates='tags')
                        
