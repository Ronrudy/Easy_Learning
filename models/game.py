#!/usr/bin/python3
""" Activity Module for EL project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.progress import Progress
from models.badge import Badge

class Game(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = 'games'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(256))
        icon_url = Column(String(256))
        activity_id = Column(String(60), ForeignKey('activities.id'), nullable=False)


        # Relationships
        badges = relationship("Badge", backref="activities")
    else:
        title = ""
        description = ""
        icon_url = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Activity"""
        super().__init__(*args, **kwargs)
