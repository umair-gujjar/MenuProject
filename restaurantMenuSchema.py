import sys

# Configuration
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# ORM defined in terms of a base class which maintains a catalog
# of classes and tables relative to that base
Base = declarative_base()

# Representation of sql tables as a Python class
class Restaurant(Base):

    # Tables
    __tablename__ = 'restaurant'

    # Mapper: Maps Python Objects to
    # columns in our database

    id = Column (
        Integer,
        primary_key = True
    )

    name = Column (
        String(80),
        nullable = False
    )

    street = Column (
    	String(80)
    )

    city = Column (
    	String(80)
    )

    state = Column (
    	String(2)
    )

    zipCode = Column (
    	Integer
    )

    phone = Column (
    	String(10)
    )

    email = Column (
    	String(50)
    )

    website = Column (
    	String(50)
    )

    cuisine = Column (
    	String(80)
    )

    description = Column (
    	String(160)
    )

    delivery = Column (
    	String(3)
    )

    @property
    def serialize(self):
        return {
        	'id' : self.id,
            'name' : self.name,
            'street' : self.street,
            'city' : self.city,
            'state' : self.state,
            'zipCode' : self.zipCode,
            'phone' : self.phone,
            'email' : self.email,
            'website' : self.website,
            'cuisine' : self.cuisine,
            'description' : self.description,
            'delivery' : self.delivery
        }

class MenuItem(Base):

    # Tables
    __tablename__ = 'menu_item'

    # Mapper: Maps Python Objects to
    # columns in our database

    id = Column (
        Integer,
        primary_key = True
    )

    name = Column (
        String(80),
        nullable = False
    )

    course = Column (
        String(80)
    )

    description = Column (
        String(160)
    )

    price = Column (
        String(10)
    )

    restaurantid = Column (
        Integer,
        ForeignKey('restaurant.id')
    )

    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        # Returns object data in serialized format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course
        }

# Insert at EOF
engine = create_engine('sqlite:///restaurantmenus.db')

Base.metadata.create_all(engine)

