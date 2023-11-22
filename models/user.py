#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from models.place import Place
from models.review


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
