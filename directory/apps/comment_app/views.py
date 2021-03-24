from .import comment
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request,jsonify
from .models import Comment
from directory import db


@comment.route('/',methods=['POST'])
@jwt_required()
def create_comment():

    if not request.is_json:
        return {"error":"JSON only!"},400

    args=request.get_json()
    identity=get_jwt_identity()

    try:
        new_comment=Comment()
        new_comment.doctor_id=args.get('doctor_id')
        new_comment.person_id=identity
        new_comment.role_sender=args.get('role_sender')
        new_comment.text=args.get('text')
        db.session.add(new_comment)
        db.session.comment()

    except ValueError as e:
        return {"error":f"{e}"},400

    return {"massage":"create comment successfully"},201

@comment.route('/',methods=['GET'])
@jwt_required()
def get_comments():
    identity=get_jwt_identity()

    comments=Comment.query.fillter(Comment.doctor_id.ilike(identity))
    comments=[{"person_id":comment.person_id,"role_sender":comment.role_sender,"text":comment.text} for comment in comments]

    return jsonify(comments)