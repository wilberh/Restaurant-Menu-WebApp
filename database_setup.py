# This Python file creates the database 3 tables: User, Restaurant, and MenuItem

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Creating the User table to track the users creating/adding items to the
# Restaurant and MenuItem tables
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Creating the Restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    menuitems = relationship('MenuItem', cascade='delete, delete-orphan')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # This method is for extracting the list of restaurants in JSON format
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


# Creating the MenuItem table
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # This method is for extracting the list of menu items in JSON format
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


# Creating the database file
engine = create_engine('sqlite:///restaurantmenuwithusers.db')


Base.metadata.create_all(engine)
