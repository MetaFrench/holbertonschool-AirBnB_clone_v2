#!/usr/bin/python3
""" New db engine """
from sqlalchemy import create_engine
# from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')
v_env = getenv('HBNB_ENV')


class DBStorage:
    """ Creates a new database """
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """ Intialization """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, database), pool_pre_ping=True)

        if v_env == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Query on current db session """
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        classDict = {'City': City, 'State': State,
                     'User': User, 'Place': Place,
                     'Review': Review, 'Amenity': Amenity}
        objects = {}
        session = self.__session
        if cls is None:
            for className in classDict:
                data = session.query(classDict[className]).all()
                for obj in data:
                    # objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
                    objects["{}.{}".format(obj.__class__.__name__,
                                           obj.id)] = obj
        else:
            if isinstance(cls, str):
                cls = classDict[cls]
            data = self.__session.query(cls).all()
            for obj in data:
                # objects[f'{obj.id}'] = obj
                objects["{}".format(obj.id)] = obj
        return objects
        # return DBStorage.__objects

    def new(self, obj):
        """add obj to current db session"""
        self.__session.add(obj)

    def save(self):
        """commit changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current db session"""
        self.__session.delete()

    def reload(self):
        """creates all tables in db"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """ Ends private session attributes """
        self.__session.close()
