#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey(
                          "places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey(
                          "amenities.id"), primary_key=True,
                          nullable=False), mysql_charset="latin1")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        user = relationship("User")
        cities = relationship("City")
        reviews = relationship("Review", cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity", viewonly=False, secondary=place_amenity,
            back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            reviews_list = []
            for key, obj in models.storage.__objects.items():
                if obj.__class__ == 'Review':
                    if obj.place_id == self.id:
                        reviews_list.append(obj)
            return reviews_list

        @property
        def amenities(self):
            amenity_list = []
            for id in amenity_ids:
                key = 'Amenity.{}'.format(id)
                if key in self.__objects.keys():
                    amenity_list.append(self.__objects[key])

        @amenities.setter
        def amenities(self, obj=None):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
            else:
                pass
