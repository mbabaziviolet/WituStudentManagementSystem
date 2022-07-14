from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class StudentApplication(db.Model):
   id: int
   application_id: int
   created_at:datetime
   updated_at:datetime
   deleted_at:datetime
    

   __tablename__ = 'StudentApplications'   
   id = db.Column(db.Integer, primary_key=True)
   application_id = db.Column(db.Integer, primary_key=True)
   created_at = db.Column(db.DateTime, default=datetime.now())
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<StudentApplications %r>" % self.id

   def tojson(self):
       return self.__dict__
