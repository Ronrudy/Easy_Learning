#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.game import Game
from models.base_model import BaseModel, Base
from models.badge import Badge
from models.activity import Activity
from models.progress import Progress
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "BaseModel": BaseModel, "Activity": Activity,
           "Badge": Badge, "Game": Game, "Progress": Progress}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        EL_MYSQL_USER = getenv('EL_MYSQL_USER')
        EL_MYSQL_PWD = getenv('EL_MYSQL_PWD')
        EL_MYSQL_HOST = getenv('EL_MYSQL_HOST')
        EL_MYSQL_DB = getenv('EL_MYSQL_DB')
        EL_ENV = getenv('EL_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EL_MYSQL_USER,
                                             EL_MYSQL_PWD,
                                             EL_MYSQL_HOST,
                                             EL_MYSQL_DB))
        if EL_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
