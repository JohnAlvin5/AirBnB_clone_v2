#!/usr/bin/python3
""" deals with storage of data in database form """

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """defines class DBStorage which initiates tables and databases """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                .format(user, passwd, host, db),
                                pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

    def new(self, obj):
    """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
    """ commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
    """ deletes from the current database session """
        if obj:
            self.session.delete(obj)

    def reload(self):
    """ creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
