from . import doctors
from .models import Doctor
from flask import request,jsonify
from directory import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity


@doctors.route('/', methods=['POST'])
def create_doctor():
    if not request.is_json:
        return {"massage": "JSON only!!"}, 400
    args = request.get_json()

    try:
        new_user = Doctor()
        new_user.name = args.get('name')
        new_user.password = args.get('password')
        new_user.role = args.get('role')
        new_user.username = args.get('username')
        new_user.number_phone = args.get('number_phone')
        new_user.specialty = args.get('specialty')
        new_user.workplace = args.get('workplace')
        new_user.city = args.get('city')
        new_user.evidence = args.get('evidence')
        new_user.address = args.get('address')

        db.session.add(new_user)
        db.session.commit()

    except ValueError as e:
        db.session.rollback()
        return {"error": f"{e}"}, 400

    except IntegrityError:
        db.session.rollback()
        return{"error": 'username is duplicate!!'}, 400

    return {"massage": "create user succesfully"}, 201


@doctors.route('/search', methods=['POST'])
@jwt_required()
def search_doctor():
    if not request.is_json:
        return{"massege": "JSON only!!"}, 400

    if not request.get_json():
        return {"massage": "JSON is empty!!"}, 400
    args = request.get_json()

    if args.get('id'):
        doc = Doctor.query.filter(Doctor.id.ilike(args.get('id')))
    if args.get('username'):
        doc = Doctor.query.filter(Doctor.username.ilike(args.get('username')))
    if args.get('name'):
        doc = Doctor.query.filter(Doctor.name.ilike(args.get('name')))
    if args.get('city'):
        doc = Doctor.query.filter(Doctor.city.ilike(args.get('city')))
    if args.get('workplace'):
        doc=doc.filter(Doctor.workplace.ilike(args.get('workplace')))
    if args.get('specialty'):
        doc=doc.filter(Doctor.specialty.ilike(args.get('specialty')))
    if args.get('evidence'):
        doc=doc.filter(Doctor.evidence.ilike(args.get('evidence')))

    doc = [{"id": doctor.id,"username":doctor.username, "name": doctor.name, "city": doctor.city, "workplace": doctor.workplace, "specialty": doctor.specialty,
            "evidence": doctor.evidence, "number_phone": doctor.number_phone, "address": doctor.address} for doctor in doc]
    return jsonify(doc)
