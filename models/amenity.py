#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import db_store
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    """Represent Amenity instances"""
    __tablename__ = "amenities"
    if db_store == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
