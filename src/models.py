import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25),unique=True)
    Population = Column(Integer)

class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25),unique=True)
    height = Column(Integer)
    mass = Column(Integer)
    planetId = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet',back_populates='characters')
    pilot = relationship('Pilot', back_populates='character')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20),unique=True)
    type = Column(String(25))
    pilot_id = Column(Integer, ForeignKey('Pilots.id'))
    pilot = relationship('Pilot', back_populates='vehicle')

class Pilot(Base):
    __tablename__ = 'pilots'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character = relationship('Character', back_populates='pilot')
    vehicle = relationship('Vehicle', back_populates='pilot')


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user__id =  Column(Integer, ForeignKey('user.id'))
    planets__id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    vehicles = Column(Integer, ForeignKey('vehicles.id'))
      




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
