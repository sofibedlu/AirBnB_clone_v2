#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if models.db_store == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            """getter for list of city instance related to state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
