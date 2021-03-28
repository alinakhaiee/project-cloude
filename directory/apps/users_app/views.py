from . import users
from flask import request,jsonify
from .models import User
from directory import db
from sqlalchemy.exc import IntegrityError,ArgumentError
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required, get_jwt_identity



@users.route("/create" ,methods=['POST'])
def create_user():
    if not request.is_json:
        return {"massage":"JSON only!!"},400
    args=request.get_json()

    try:
        new_user=User()
        new_user.name=args.get('name')
        new_user.password=args.get('password')
        new_user.role=args.get('role')
        new_user.username=args.get('username')
        new_user.number=args.get('number')

        db.session.add(new_user)
        db.session.commit()

    except ValueError as e:
        db.session.rollback()
        return {"error":f"{e}"},400

    except IntegrityError:
        db.session.rollback()
        return{"error":'username is duplicate!!'},400
    
    return {"massage":"create user succesfully"},201

@users.route('/auth',methods=['POST'])
def login():
    if not request.is_json:
        return{"massege": "JSON only!!"}, 400
    if not request.get_json():
        return {"massage":"JSON is empty!!"}
    args=request.get_json()
    username=args.get('username')
    password=args.get('password')

    user=User.query.filter(User.username.ilike(username)).first()
    if not user:
        return {"error": "username or password not match!"}, 403
    if not user.check_password(password):
        return {"error": "username or password not match!"}, 403

    access_token=create_access_token(identity=user.id,fresh=True)
    refresh_token=create_refresh_token(identity=user.id)

    return {"access_token":access_token,"refresh_token":refresh_token},200


@users.route('/modify',methods=['PATCH'])
@jwt_required()
def modify_user():
    if not request.is_json:
        return{"massege": "JSON only!!"}, 400
    
    if not request.get_json():
        return {"massage":"JSON is empty!!"},400
    args=request.get_json()
    identity = get_jwt_identity()
    user = User.query.filter(User.id.ilike(identity)).first()

    try:
        if not args.get('role') is None:
              user.role=args.get('role')
        if not args.get('number') is None:
            user.number=args.get('number')
        if not args.get('name') is None:
            user.name=args.get('name')
        db.session.commit()
    except ValueError as e:
        return {"error":f"{e}"},400
    return {},204



@users.route('/get', methods=['GET'])
@jwt_required()
def get_user():
    identity = get_jwt_identity()
    user = User.query.filter(User.id.ilike(identity)).first()
    return {"username": user.username,"number":user.number,"role":user.role,"name":user.name,}


@users.route('/getfavorite', methods=['GET'])
@jwt_required()
def get_favorite():
    identity = get_jwt_identity()
    user = User.query.filter(User.id.ilike(identity)).first()
    user=[{"doctor_id":id.doctor_id,"person_id":id.person_id} for id in user.favorite_doctor]
    return jsonify(user)

@users.route('/auth/',methods=['PUT'])
@jwt_required(refresh=True)
def refresh_token():
    identity=get_jwt_identity()
    return {"access_token":create_access_token(identity=identity)}