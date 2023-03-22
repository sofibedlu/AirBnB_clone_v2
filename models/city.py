#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.db_storage == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForignKey('states.id') nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initalize city"""
        super().__init__(*args, **kwargs)
