#!/usr/bin/python3
"""These is DBStorage class"""

import sqlalchemy
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review}


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
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
            return new_dict
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        if obj is not None:
            try:
                self.__session.add(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            cls = obj.__class__.__name__
            self.__session.query(cls).filter(
                    cls.id == obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        ss_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(ss_maker)()
