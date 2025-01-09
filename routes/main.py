from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint


main_route = Blueprint("main", __name__)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Access API"}
)
main_route.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
