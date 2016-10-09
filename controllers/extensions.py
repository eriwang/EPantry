from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *

SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'mysql://' + config.env['user'] + env('password') + '@' + env('host') + ':' + env('port') + '/' + \
                          env('db')

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base(engine)

class User(Base):
	__tablename__ = "user"
	__table_args__ = {'autoload':True}

class Pantry(Base):
	__tablename__ = "pantry"
	__table_args__ = {'autoload': True}

class Recipe(Base):
	__tablename__ = "recipe"
	__table_args__ = {'autoload': True}

class Item(Base):
	__tablename__ = "item"
	__table_args__ = {'autoload': True}

class Stock(Base):
	__tablename__ = "stock"
	__table_args__ = {'autoload': True}

class Possible_Recipe(Base):
	__tablename__ = "possible_recipe"
	__table_args__ = {'autoload': True}

class Recipe_Requirement(Base):
	__tablename__ = "recipe_requirement"
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