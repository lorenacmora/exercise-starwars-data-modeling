import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)

    def created(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    poblacion = Column(String(50), nullable=False)
    diametro = Column(String(50), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Characters(Base):
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    altura = Column(String(50), nullable=False)
    otros = Column(String(50), nullable=False)
    def speak():
        return{}
    def fight():
        return{}


class Tipo(enum.Enum):
    planets = "planets"
    characters = "characters"

class Favorites(Base):
    __tablename__ = "Favorites"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, nullable=False)
    tipo_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    tipo = Column("tipo",Enum(Tipo))
    
    def add_favorites():
        return {}


render_er(Base, 'diagram.png')




