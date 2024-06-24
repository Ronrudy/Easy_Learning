#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        username = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        age = Column(Integer, nullable=False)
        class_level = Column(String(60), nullable=False)
        
        # Relationships
        games = relationship("Game", backref="user")
        progress = relationship("Progress", backref="user")
        badges = relationship("Badge", backref="user")
    else:
        username = ""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        age = ""
        class_level = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
