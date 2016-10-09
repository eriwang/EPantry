from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

#SQLALCHEMY_DATABASE_URI = 'mysql://' + config.env['user'] + config.env['password'] + '@' + \
 #                         config.env['host'] + ':' + config.env['port'] + '/' + config.env['db']

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3000/EPANTRY'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base(engine)

class User(Base):
	__tablename__ = "user"
	__table_args__ = {'autoload':True}
	def __init__(self, email):
		self.email = email

class Pantry(Base):
	__tablename__ = "pantry"
	__table_args__ = {'autoload': True}
	def __init__(self, email):
		self.user_email = email

class Recipe(Base):
	__tablename__ = "recipe"
	__table_args__ = {'autoload': True}
	def __init__(self, name, email, recipe_instruct):
		self.name = name, self.user_email = email, self.recipe_instruct = recipe_instruct
class Item(Base):
	__tablename__ = "item"
	__table_args__ = {'autoload': True}
	def __init__(self, amount, unit, stock_name ):
		self.amount = amount, self.unit = unit, self.stock_name = stock_name

class Stock(Base):
	__tablename__ = "stock"
	__table_args__ = {'autoload': True}
	def __init__(self, name, amount, unit, pantry_id):
		self.amount = amount, self.name = name, self.unit = unit, self.pantry_id = pantry_id

class Possible_Recipe(Base):
	__tablename__ = "possible_recipe"
	__table_args__ = {'autoload': True}
	def __init__(self, stock_name, recipe_name):
		self.stock_name = stock_name, self.recipe_name = recipe_name

class Recipe_Requirement(Base):
	__tablename__ = "recipe_requirement"
	__table_args__ = {'autoload': True}
	def __init__(self, quantity, unit, stock_name, recipe_name):
		self.quantity = quantity, self.unit = unit, self.stock_name = stock_name, self.recipe_name = recipe_name


def loadSession():
	metadata = Base.metadata
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