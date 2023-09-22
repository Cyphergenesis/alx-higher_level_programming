#!/usr/bin/python3
"""Defines the City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """Represents a city in the database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

