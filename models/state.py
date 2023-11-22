#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel,Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import shlex
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                        backref="state")
