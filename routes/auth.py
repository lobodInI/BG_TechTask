from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User


auth_route = Blueprint("auth", __name__)

@auth_route.route("/auth/register/", methods=["POST"])
def signup() -> tuple[Response, int]:
    data = request.get_json()

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    if not all([first_name, last_name, email, password]):
        return jsonify({"message": "All fields must be filled in!"}), 400

    user_db = User.query.filter_by(email=email).first()

    if user_db:
        return jsonify({"message": f"User with email: {email} already exists!"}), 400

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=generate_password_hash(password=password)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User signup successful!"}), 200


@auth_route.route("/auth/login/", methods=["POST"])
def login() -> tuple[Response, int]:
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user_db = User.query.filter_by(email=email).first()

    if not user_db:
        return jsonify({"message": f"User with email: {email} not found!"}), 404

    if not check_password_hash(user_db.password, password):
        return jsonify({"message": "Password does not match!"}), 400

    return jsonify(
        {
            "message": "Login successful!",
            "access": create_access_token(identity=str(user_db.id)),
            "refresh": create_refresh_token(identity=str(user_db.id)),
        }
    ), 200


@auth_route.route("/auth/me/", methods=["GET"])
@jwt_required()
def info_about_me():
    current_user = User.query.get(get_jwt_identity())

    return jsonify(
        {"message": f"Info about me: {current_user.to_json()}"}
    )
