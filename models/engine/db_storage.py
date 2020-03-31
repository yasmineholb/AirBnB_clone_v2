#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""



class DBstorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine):  SQLAlchemy engine.
        __session (sqlalchemy.Session): SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        pass