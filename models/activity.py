#!/usr/bin/python3
""" ActivityCategory Module for EL project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.progress import Progress
from models.game import Game

if models.storage_t == 'db':
    user_activity = Table('user_activity', Base.metadata,
                          Column('user_id', String(60),
                                 ForeignKey('users.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('activity_id', String(60),
                                 ForeignKey('activities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Activity(BaseModel, Base):
    """Representation of activity """
    if models.storage_t == 'db':
        __tablename__ = 'activities'
        name = Column(String(60), nullable=False)
        description = Column(String(200))
        icon_url = Column(String(256))


        # Relationships
        Progress = relationship("Progress", backref="activity")
        games = relationship("Game", backref="activity")
        users = relationship("User", secondary="user_activity",
                                 backref="users_activities",
                                 viewonly=False)
   
    else:
        name = ""
        description = ""
        icon_url = ""
        user_ids = []

    def __init__(self, *args, **kwargs):
        """initializes ActivityCategory"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def games(self):
            """getter attribute returns the list of Game instances"""
            from models.game import Game
            game_list = []
            all_games = models.storage.all(Game)
            for game in all_games.values():
                if game.activity_id == self.id:
                    game_list.append(game)
            return game_list

        @property
        def users(self):
            """getter attribute returns the list of User instances"""
            from models.user import User
            user_list = []
            all_users = models.storage.all(User)
            for user in all_users.values():
                if user.activity_id == self.id:
                    user_list.append(user)
            return user_list
        
        

    