from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class Program(db.Model):
   id: int
   name: str
   description: str
   start_date: date
   end_date: date
   duration: str
   status:str
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'Programs'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   description = db.Column(db.Text(120), unique=True, nullable=True)
   start_date = db.Column(db.Date(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   start_date = db.Column(db.Date(), nullable=False)
   end_date = db.Column(db.Date(), nullable=False)
   status = db.Column(db.Date(), nullable=False,default="Inprogress")
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Program %r>" % self.name

   def tojson(self):
       return self.__dict__
