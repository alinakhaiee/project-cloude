from sqlalchemy import Column,Integer
from sqlalchemy.orm import validates
from directory import db

class FavoriteDoctor(db.Model):
    __tablename__="FavoriteDoctors"
    doctor_id=Column(Integer(),unique=False,nullable=False)
    person_id=Column(Integer(),unique=False,nullable=False)
    __mapper_args__ = {
        'primary_key':[doctor_id,person_id]
    }

    @validates('doctor_id')
    def validate_doctor_id(self,key,value):
        if value is None:
            raise ValueError("doctor_id can not null!!!")
        return value

    @validates('person_id')
    def validate_person_id(self,key,value):
        if value is None:
            raise ValueError("person_id can not null!!!")
        return value