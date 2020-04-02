#!/usr/bin/python3
"""This is the review class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__ (str): MySQL table name to store Reviews.
        text (sqlalchemy String): review description.
        place_id (sqlalchemy String): review's place id.
        user_id (sqlalchemy String): review's user id.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
