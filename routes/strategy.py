from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, TradingStrategy


strategies_route = Blueprint("strategies", __name__)

@strategies_route.route("/strategies/", methods=["GET"])
@jwt_required()
def get_all_strategies() -> tuple[Response, int]:
    all_user_strategies = TradingStrategy.query.filter_by(owner_id=get_jwt_identity())

    return jsonify(
        {"strategies": [strategy.to_json() for strategy in all_user_strategies]}
    ), 200


@strategies_route.route("/strategies/", methods=["POST"])
@jwt_required()
def create_strategies() -> tuple[Response, int]:
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    asset_type = data.get("asset_type")
    buy_condition = data.get("buy_condition")
    sell_condition = data.get("sell_condition")
    status = data.get("status")

    if not all([name, asset_type, buy_condition, sell_condition, status]):
        return jsonify(
            {"message": "Fields (name, asset_type, buy_condition, sell_condition, status) "
                        "must be filled in!"}
        ), 400

    new_strategy = TradingStrategy(
        name=name,
        description=description,
        asset_type=asset_type,
        buy_condition=buy_condition,
        sell_condition=sell_condition,
        status=status,
        owner_id=get_jwt_identity()
    )

    db.session.add(new_strategy)
    db.session.commit()

    return jsonify({"message": "New strategy added!"}), 201
