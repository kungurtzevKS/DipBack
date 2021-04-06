import builtins
import json

import sqlalchemy
from Models import *

from sqlalchemy import create_engine
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app import db


mess_agregator = Blueprint('mess_agregator', __name__)
@mess_agregator.route('/')
def index():
    return "hello world"

@mess_agregator.route('/clients')
def clients():
    user = Users.query.all()
    user = [{"id":users.id, "Firstname":users.Firstname} for users in user]
    return jsonify(user)

@mess_agregator.route('/login', methods=["POST"])
def login():
    data = request.data
    data = json.loads(data)
    print(data)
    if Users.query.filter_by(login=data["login"]).first():
        if Users.query.filter_by(password=data["password"]).first():
            user = Users.query.filter_by(login=data["login"]).first()
            identity = user.toJson()
            access_token = create_access_token(identity=identity)
            return jsonify({"jwt":access_token})
        else:
            return 401
    else: return 502

@mess_agregator.route('/registration', methods=["POST"])
def registration():
    data = request.data
    data = json.loads(data)

    if Users.query.filter_by(login=data["login"]).first():
        return "", 403
    else:
        guest = Users(login=data["login"], password=data["password"], Firstname=data["Firstname"], Secondname=data["Secondname"])
        try:
            db.session.add(guest)
            db.session.commit()

            identity = guest.toJson()
            access_token = create_access_token(identity=identity)
            return jsonify({"jwt":access_token})
        except:
            return 502

@mess_agregator.route('/mail_add', methods=["POST"])
def mail_add():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.filter_by(login=data["login"]).first()
        user.mail = data["mail"]
        try:
            db.session.add(user)
            db.session.commit()
            return 201
        except:
            return 502
    else: return 502

@mess_agregator.route('/photo_add', methods=["POST"])
def photo_add():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.filter_by(login=data["login"]).first()
        user.avatar_name = data["avatar_name"]
        try:
            db.session.add(user)
            db.session.commit()
            return 201
        except:
            return 502
    else: return 502

@mess_agregator.route('/VKToken_add', methods=["POST"])
def VKToken_add():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.query.filter_by(login=data["login"]).first()
        user.VKToken = data["VKToken"]
        try:
            db.session.add(user)
            db.session.commit()
            return "", 201
        except:
            return "", 502
    else:
        return 502

@mess_agregator.route('/FBToken_add', methods=["POST"])
def FBToken_add():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.query.filter_by(login=data["login"]).first()
        user.FBToken = data["FBToken"]
        try:
            db.session.add(user)
            db.session.commit()
            return 201
        except:
            return 502
    else:
        return 502

@mess_agregator.route('/TGToken_add', methods=["POST"])
def TGToken_add():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.filter_by(login=data["login"]).first()
        user.TGToken = data["TGToken"]
        try:
            db.session.add(user)
            db.session.commit()
            return 201
        except:
            return 502
    else:
        return 502

@mess_agregator.route('/rename', methods=["POST"])
def rename():
    data = request.data
    data = json.loads(data)
    if Users.query.filter_by(login=data["login"]).first():
        user = Users.filter_by(login=data["login"]).first()
        user.Firstname = data["Firstname"]
        user.Secondname = data["Secondname"]
        try:
            db.session.add(user)
            db.session.commit()
            return 201
        except:
            return 502
    else:
        return 502