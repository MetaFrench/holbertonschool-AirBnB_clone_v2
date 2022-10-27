#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
=======
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()


else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
>>>>>>> efbf42c22502b8589acf0b08781b921a80392a0e
