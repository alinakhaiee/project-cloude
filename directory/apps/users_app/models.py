from sqlalchemy import Column,Integer,String,DECIMAL
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash,check_password_hash
from directory import db



class User(db.Model):
    __tablename__="users"
    id=Column(Integer(), primary_key=True)
    username=Column(String(32),unique=True,nullable=False)  # code meli
    password=Column(String(128),unique=False,nullable=False)
    role=Column(String(32),unique=False,nullable=False)
    name=Column(String(32),unique=False,nullable=False)
    number=Column(String(32),unique=False,nullable=False)



    @validates("password")
    def validate_pass(self,key,value):
        if value is None:
            raise ValueError('password can not null!!')
        if len(value)<6:
             raise ValueError('password atleast 6 charcters!!!')
        return generate_password_hash(value)

    @validates('name')
    def validate_name(self,key,value):
        if value is None:
             raise ValueError('name can not null!!')
        return value

    @validates('username')
    def validate_user_name(self,key,value):
        if value is None:
            raise ValueError('username can not null!!')
        if len(value)<10:
            raise ValueError('username atleast 10 charcters!!!')
        return value
    @validates('role')
    def validate_role(self,key,value):
        if value is None:
            raise ValueError('role can not null!!')
        return value

    @validates('number')
    def validate_number(self,key,value):
        if value is None:
            raise ValueError('role can not null!!')
        if len(value)<11:
            raise ValueError('number atleast 11 charcters!!!')
        return value


    def check_password(self,password):
        return check_password_hash(self.password,password)

