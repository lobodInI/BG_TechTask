from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Configurator
from models import db
from routes.main import main_route


def create_app():
    app = Flask(__name__, static_folder="static")

    Configurator.init_flask_config(app=app)

    jwt = JWTManager(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()

        migrate = Migrate(app, db)

    app.register_blueprint(main_route)

    return app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)
