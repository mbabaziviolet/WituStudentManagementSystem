from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class Admin(db.Model):
   id: int
   email: str
   password: str
   name:str
   created_at:datetime
   updated_at:datetime
   __tablename__ = 'admins'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.Text(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Admin %r>" % self.name

   def tojson(self):
       return self.__dict__
