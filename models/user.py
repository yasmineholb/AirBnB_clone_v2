#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        __tablename__ (str): MySQL table name to store users.
        email: (sqlalchemy String): User email address.
        password (sqlalchemy String): User password.
        first_name (sqlalchemy String): User first name.
        last_name (sqlalchemy String): User last name.
        places (orm relationship): User-Place relationship.
        reviews (orm relationship): User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
