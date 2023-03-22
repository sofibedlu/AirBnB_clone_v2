#!/usr/bin/python3
"""These is DBStorage class"""
import os
import sqlalchemy
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.base_model import BaseModel, Base

classes = {"State": State, "City": City, "User": User,
           "Place": Place}


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """public instance for DBStorage class"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB,
                                              pool_pre_ping=True))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects depending of the class name"""
        new_dict = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objs = self.__session.query(classes[clas]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        ss_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ss_maker)
        self.__session = Session
