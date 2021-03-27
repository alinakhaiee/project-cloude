from sqlalchemy import Column,Integer,String,Text,DateTime,ForeignKey
from directory import db
import datetime as dt
from sqlalchemy.orm import validates,relationship




class Comment(db.Model):
    __tablename__="comments"
    id=Column(Integer(),primary_key=True)
    doctor_id=Column(Integer(),unique=False,nullable=False)
    person_id=Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    text=Column(Text(),unique=False,nullable=False)
    create_data=Column(DateTime(),unique=False,nullable=False,default=dt.datetime.utcnow)
    users = relationship("User", back_populates="comment")

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
