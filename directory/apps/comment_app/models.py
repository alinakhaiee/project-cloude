from sqlalchemy import Column,Integer,String,Text,DateTime
from directory import db
import datetime as dt
from sqlalchemy.orm import validates




class Comment(db.Model):
    id=Column(Integer(),primary_key=True)
    doctor_id=Column(Integer(),unique=False,nullable=False)
    person_id=Column(Integer(),unique=False,nullable=False)
    role_sender=Column(String(32),unique=False,nullable=False)
    text=Column(Text(),unique=False,nullable=False)
    create_data=Column(DateTime(),unique=False,nullable=False,default=dt.datetime.utcnow)

    @validates('doctor_id')
    def validate_doctor_id(self,key,value):
        if value is None:
            raise ValueError('doctor_id can not null!!')
        return value

    @validates('person_id')
    def validate_person_id(self,key,value):
        if value is None:
            raise ValueError('person_id can not null!!')
        return value

    @validates('role_sender')
    def validate_role_sender(self,key,value):
        if value is None:
            raise ValueError('role_sender can not null!!')
        return value
    @validates('text')
    def validate_text(self,key,value):
        if value is None:
            raise ValueError('text comment can not null!!')
        return value
