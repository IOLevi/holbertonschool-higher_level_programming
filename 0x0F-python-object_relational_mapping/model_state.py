#!/usr/bin/env python3
#contains the class definition of a State and an instance of Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name =  Column("name", String(128), nullable=False)