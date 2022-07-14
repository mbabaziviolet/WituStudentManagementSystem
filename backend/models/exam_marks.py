from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class ExamMarks(db.Model):
   id: int
   mark_id: int
   created_at:datetime
   deleted_at:datetime
   updated_at:datetime

   __tablename__ = 'ExamMarks'   
   id = db.Column(db.Integer, primary_key=True)
   mark_id = db.Column(db.Integer, primary_key=True)
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<ExamMarks %r>" % self.id

   def tojson(self):
       return self.__dict__
