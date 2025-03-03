#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.rom import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    place = relationship("Place", cascade='all, delete, delete-orphan',
            backref="cities")
