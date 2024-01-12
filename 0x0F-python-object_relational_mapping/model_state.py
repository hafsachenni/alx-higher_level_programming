#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    creates state class
    links to the MySQL table states
    class attribute id that represents a column
    class attribute name that represents a column
     must use the module SQLAlchemy
     should connect to a MySQL server running on localhost at port 3306
     """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
