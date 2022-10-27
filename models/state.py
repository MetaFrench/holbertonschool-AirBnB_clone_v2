#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # sets relationship between state and city
        cities = relationship('City', backref='state',
                                cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """returns list of City instances associated with state.id"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
