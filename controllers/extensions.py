from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base(engine)

class User(Base):
	__tablename__ = "User"
	__table_args__ = {'autoload':True}

class Pantry(Base):
	__tablename__ = "Pantry"
	__table_args__ = {'autoload': True}

class Recipe(Base):
	__tablename__ = "Recipe"
	__table_args__ = {'autoload': True}

class Item(Base):
	__tablename__ = "Item"
	__table_args__ = {'autoload': True}

class Stock(Base):
	__tablename__ = "Stock"
	__table_args__ = {'autoload': True}

def loadSession():
	metadata = Base.metada
	Session = sessionmaker(bind = engine)
	session = Session()
	return session

#def connect_to_database():
  #host = 'localhost'
  #port = 3000
  #client = MongoClient(host, port)
  #db = client.test_database
  #return db

#db = connect_to_database()