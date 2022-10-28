#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD

import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
=======
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

>>>>>>> eb23d18bb1f999dedba2525a6e0151d9bcfeb3a6
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
