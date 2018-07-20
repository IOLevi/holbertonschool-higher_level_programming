#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SomeClass(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, )
    name =  Column(String(128), nullable=False)
    
