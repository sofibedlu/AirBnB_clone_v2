#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class Place(BaseModel, Base):
    """ A place to stay """
    if models.db_store == "db":
        __tablename__ = 'places'
        city_id = Column(string(60), ForeignKey(cities.id), nullable=False)
        user_id = Column(string(60), ForeignKey(users.id), nullable=False)
        name = Column(string(128), nullable=False)
        description = Column(string(128), nullable=False)
        number_rooms = 
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
