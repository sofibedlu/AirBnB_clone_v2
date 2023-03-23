#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

if models.db_store == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if models.db_store == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False,
                              default=0)
        number_bathrooms = Column(Integer, nullable=False,
                                  default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False,
                                default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenity_ids = []
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False, backref='place_amenities')

    else:
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

        @property
        def review(self):
            """getter method"""
            from models import storage
            rev_list = []
            for obj in storage.all('Review').values():
                if obj.place_id == self.id:
                    rev_list.append(obj)
            return rev_list

        @property
        def amenities(self):

            """getter method"""
            from models import storage
            ameni_list = []
            for obj in storage.all('Amenity').values():
                if obj.id in self.amenity_ids:
                    ameni_list.append(obj)
            return ameni_list

        @amenities.setter
        def amenities(self, obj):
            if obj is not None and isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
