#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models
from os import getenv

db_store = getenv("HBNB_TYPE_STORAGE")

if db_store == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
