from . import favorite_doctor
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request,jsonify
from .models import FavoriteDoctor
from directory import db




@favorite_doctor.route('/',methods=['POST'])
@jwt_required()
def add_favorite_doctor():
    if not request.is_json:
        return {"error":"JSON only!"},400
    args=request.get_json()
    identity=get_jwt_identity()

    try:
        new_FavoriteDoctor=FavoriteDoctor()
        new_FavoriteDoctor.doctor_id=args.get('doctor_id')
        new_FavoriteDoctor.person_id=identity
        db.session.add(new_FavoriteDoctor)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return {"error":f"{e}"},400
    
    return {"massage":"add doctor in favorite successfully"},201


@favorite_doctor.route('/',methods=['GET'])
@jwt_required()
def get_favorite_doctors():
     identity=get_jwt_identity()
     doctors=FavoriteDoctor.query.filter(FavoriteDoctor.username.ilike(identity))
     doctors=[{"doctor_id":doctor.doctor_id} for doctor in doctors]

     return jsonify(doctors)

