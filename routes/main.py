from flask import Blueprint, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from routes.auth import auth_route
from routes.strategy import strategies_route


main_route = Blueprint("main", __name__)

SWAGGER_URL = "/swagger/"
API_URL = "/static/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Access API"}
)
main_route.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
main_route.register_blueprint(auth_route)
main_route.register_blueprint(strategies_route)


@main_route.route("/health_check/", methods=["GET"])
def health_check():
    return jsonify({"message": "API working"}), 200
