#!/usr/bin/python3
""" Progress module for the EL project """
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float
from models.user import User
import time
from sqlalchemy.orm import relationship


class Progress(BaseModel, Base):
    """ Progress class to store review information """
    if models.storage_t == 'db':
        __tablename__ = 'progress'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        activity_id = Column(String(60), ForeignKey('activities.id'), nullable=False)
        progress_percent = Column(Float)

        # Relationships

    else:
        user_id = ""
        activity_id = ""
        progress_percent = ""
        

    def __init__(self, *args, **kwargs):
        """initializes Progress"""
        super().__init__(*args, **kwargs)
