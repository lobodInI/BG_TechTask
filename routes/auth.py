from flask import Blueprint, session, request, jsonify, Response
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

    return jsonify({"message": "Login successful!"}), 200
