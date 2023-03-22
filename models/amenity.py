#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import db_store
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    """Represent Amenity instances"""
    if db_store == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
