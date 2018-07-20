#!/usr/bin/env python3
#contains the class definition of a City and an instance of Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State

class City(Base):
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name =  Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'), nullable=False,)