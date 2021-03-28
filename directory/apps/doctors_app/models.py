from sqlalchemy import Column,Integer,String,Text,ForeignKey,DateTime
from directory import db
from sqlalchemy.orm import validates,relationship
from werkzeug.security import generate_password_hash


class Doctor(db.Model):
    __tablename__="doctors"
    id=Column(Integer(),primary_key=True)
    name=Column(String(32),unique=False,nullable=True)
    username=Column(String(32),unique=True,nullable=False)
    city=Column(String(32),unique=False,nullable=False)
    password=Column(String(128),unique=False,nullable=False)
    workplace=Column(String(32),unique=False,nullable=False)
    role=Column(String(32),unique=False,nullable=True)
    specialty=Column(String(32),unique=False,nullable=False)
    evidence=Column(String(32),unique=False,nullable=False)
    number_phone=Column(String(32),unique=False,nullable=True)
    address=Column(Text(),unique=False,nullable=True)
    visit_doctor=relationship('VisitDoctor',backref='doctor',cascade="all, delete",passive_deletes=True)

    @validates('username')
    def validate_username(self,key,value):
        if value is None:
            raise ValueError("username can not null!!")
        return value

    @validates("password")
    def validate_pass(self,key,value):
        if value is None:
            raise ValueError('password can not null!!')
        if len(value)<6:
             raise ValueError('password atleast 6 charcters!!!')
        return generate_password_hash(value)

    @validates('city')
    def validate_city(self,key,value):
        if value is None:
            raise ValueError("city can not null!!")
        return value
    
    @validates('specialty')
    def validate_specialty(self,key,value):
        if value is None:
            raise ValueError("specialty can not null!!")
        return value

    @validates('evidence')
    def validate_evidence(self,key,value):
        if value is None:
            raise ValueError("evidence can not null!!")
        return value

    @validates('workplace')
    def validate_workplace(self,key,value):
        if value is None:
            raise ValueError("workplace can not null!!")
        return value

class VisitDoctor(db.Model):
    id=Column(Integer(),primary_key=True)
    doctor_id=Column(Integer(),ForeignKey('doctors.id', ondelete="CASCADE"))
    person_id=Column(Integer(),ForeignKey('users.id', ondelete="CASCADE"))
    time_visit=Column(DateTime(),unique=False,nullable=False)


    @validates('doctor_id')
    def validate_specialty(self,key,value):
        if value is None:
            raise ValueError("doctor_id can not null!!")
        return value

    @validates('person_id')
    def validate_evidence(self,key,value):
        if value is None:
            raise ValueError("person_id can not null!!")
        return value

    @validates('time_visit')
    def validate_workplace(self,key,value):
        if value is None:
            raise ValueError("time_visit can not null!!")
        return value