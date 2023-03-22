#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import models
from models.base_model import BaseModel
from models.base_mode import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.db_store == "db":
        __tablename = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)

    if models.db_store != "db":
        @property
        def cities(self):
            """getter for list of city instance related to state"""
            city_list[] = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
