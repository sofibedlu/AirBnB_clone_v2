#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
<<<<<<< HEAD
=======
from models.place import Place

>>>>>>> 4a2919e46645f5a71afd31fc6ff82b249e42252a

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.db_store == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initalize user class"""
        super().__init__(*args, **kwargs)
