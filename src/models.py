import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)
    email=Column(String(250), nullable=False)

    
    favorites_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)

    def sign():
        return {}
    def editProfile():
        return {}
    def like():
        return {}
    def favorites():
        return {}
    def notFavorites():
        return {}
    def comment():
        return {}
    def close():
        return {}
    def notLike():
        return {}


# class Admin(Base):
#     __tablename__ = 'admin'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     password=Column(String(250), nullable=False)
#     email=Column(String(250), nullable=False)

#     def modify():
#        return {}

class Favorites (Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)


   
class Characters (Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    birthYear=Column(String(250), nullable=False)
    species=Column(String(250), nullable=False)
    height=Column(String(250), nullable=False)
    mass=Column(String(250), nullable=False)
    gender=Column(String(250), nullable=False)
    hairColor=Column(String(250), nullable=False)
    skinColor=Column(String(250), nullable=False)
    homeworld=Column(String(250), nullable=False)
		
    relatedFilms=Column(String(250), nullable=False)
    relatedVehicles=Column(String(250), nullable=False)
    relatedStarships=Column(String(250), nullable=False)
 
 

# class Films (Base):
#     __tablename__ = 'films'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

#     dateCreated=Column(String(250), nullable=False)
#     director=Column(String(250), nullable=False)
#     producer=Column(String(250), nullable=False)
#     openingCrawl=Column(String(250), nullable=False)
		
#     relatedCharacters=Column(String(250), nullable=False)
#     relatedStarships=Column(String(250), nullable=False)
#     relatedSpecies=Column(String(250), nullable=False)
#     relatedPlanets=Column(String(250), nullable=False)
#     relatedVehicles=Column(String(250), nullable=False)

 

class Species (Base):
    __tablename__ = 'species'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    classification=Column(String(250), nullable=False)
    designation=Column(String(250), nullable=False)
    language=Column(String(250), nullable=False)
    avgLifespan=Column(String(250), nullable=False)
    avgHeight=Column(String(250), nullable=False)
    hairColor=Column(String(250), nullable=False)
    skinColor=Column(String(250), nullable=False)
    eyeColor=Column(String(250), nullable=False)
		
    relatedFilms=Column(String(250), nullable=False)
    relatedCharacters=Column(String(250), nullable=False)

# class Starships (Base):
#     __tablename__ = 'starships'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     model= Column(String(250), nullable=False)
#     manufacturer= Column(String(250), nullable=False)
#     classN= Column(String(250), nullable=False)
#     cost= Column(String(250), nullable=False)
#     speed= Column(String(250), nullable=False)
#     hyperdriveRating= Column(String(250), nullable=False)
#     mGLT= Column(String(250), nullable=False)
#     length= Column(String(250), nullable=False)
#     cargoCapacity= Column(String(250), nullable=False)
#     mimimum= Column(String(250), nullable=False)
#     passengers= Column(String(250), nullable=False)

#     relatedFilms= Column(String(250), nullable=False)
#     relatedPilots= Column(String(250), nullable=False)

# class Vehicles (Base):
#     __tablename__ = 'vehicles'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     model= Column(String(250), nullable=False)
#     manofacturer= Column(String(250), nullable=False)
#     classN= Column(String(250), nullable=False)
#     speed= Column(String(250), nullable=False)
#     cost= Column(String(250), nullable=False)
#     length= Column(String(250), nullable=False)
#     cargoCapacity= Column(String(250), nullable=False)
#     mimumCrew= Column(String(250), nullable=False)
#     passengers= Column(String(250), nullable=False)

#     relatedFilms= Column(String(250), nullable=False)
#     relatedPilots= Column(String(250), nullable=False)
   


#  class Starships (Base):
#     __tablename__ = 'starships'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

#     model
#     manufacturer
#     classN
# 	cost
# 	speed
# 	hyperdriveRating
# 	mGLT
# 	length
# 	cargoCapacity
# 	mimimum
# 	passengers

	# //relatedFilms
    # relatedPilots

  

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')