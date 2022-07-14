from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class TimeTable(db.Model):
   id: int
   name: str
   description: str
   start_time:date
   end_time:date
   day:date
   duration:str
   status:str
   is_submitted:bool
   created_at:datetime
   updated_at:datetime
   deleted_at:datetime
   posted_at:datetime

   __tablename__ = 'TimeTables'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   description = db.Column(db.Text(120), unique=True, nullable=True)
   course_unit_id = db.Column(db.Integer, db.ForeignKey('course_units.id',ondelete='CASCADE'))
   start_time = db.Column(db.Date, default=date.now())
   end_time = db.Column(db.Date, default=date.now())
   day = db.Column(db.Date, default=date.now())
   duration = db.Column(db.String(80), nullable=False)
   status = db.Column(db.String(80), nullable=False)
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   posted_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<TimeTable %r>" % self.name

   def tojson(self):
       return self.__dict__
