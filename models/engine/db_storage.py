#!/usr/bin/python3
"""
Storage module
"""
import datetime
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review,
               }


class DBStorage():
    """
    DBStorage class
    """
    # Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """
        init method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ all method """
        obj_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                obj_dict.update({f'{type(cls).__name__}.{obj.id}': obj})
        else:
            for class_name in all_classes.values():
                obj_list = self.__session.query(class_name)
                for obj in obj_list:
                    obj_dict.update({f'{type(obj).__name__}.{obj.id}': obj})
        return obj_dict

    def new(self, obj):
        """
        add object to current session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        creates all tables
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        close session
        """
        self.__session.remove()
