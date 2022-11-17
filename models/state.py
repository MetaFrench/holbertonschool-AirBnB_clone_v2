#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade='all, delete, delete-orphan')

    else:
        @property
        def cities(self):
            """getter for cities"""
            city_list = []
            for stuff in models.storage.all(City).values():
                if stuff.state_id == self.id:
                    city_list.append(stuff)
            return city_list
