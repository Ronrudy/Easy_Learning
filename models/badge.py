#!/usr/bin/python
""" holds class Badge"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Badge(BaseModel, Base):
    """Representation of badge """
    if models.storage_t == "db":
        __tablename__ = 'badges'
        description = Column(String(200))
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        game_id = Column(String(60), ForeignKey('games.id'), nullable=False)
        badge_name = Column(String(128))
        icon_url = Column(String(256))
        date_awarded = datetime.now()
        
        # Relationships

    else:
        description = ""
        user_id = ""
        game_id = ""
        badge_name = ""
        date_awarded = ""
        icon_url = ""

    def __init__(self, *args, **kwargs):
        """initializes badge"""
        super().__init__(*args, **kwargs)
