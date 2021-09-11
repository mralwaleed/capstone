from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os


from sqlalchemy.sql.sqltypes import Integer, Date


database_path = 'postgres://bwzoeiwpvzwgct:022d2874c3dea5f4a70d683308c00242c95568e1bfde5f9942342b0d32f363ef@ec2-44-196-8-220.compute-1.amazonaws.com:5432/dfqafbqm2cva38'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Movies(db.Model):  
  __tablename__ = 'Movies'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  release_date = Column(Date,  nullable=False)

class Actors(db.Model):  
  __tablename__ = 'Actors'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(String,  nullable=False)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}