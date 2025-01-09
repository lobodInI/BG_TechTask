from environs import Env
from flask import Flask

class Configurator:

    @staticmethod
    def init_flask_config(app: Flask) -> None:
        env = Env()
        env.read_env(".env")

        app.config["SECRET_KEY"] = env("SECRET_KEY")

        sql_driver = env("SQL_DRIVER")
        db_host = env("DB_HOST")
        db_port = env("DB_PORT")
        db_user = env("DB_USER")
        db_pass = env("DB_PASSWORD")
        db_name = env("DB_NAME")

        app.config["SQLALCHEMY_DATABASE_URI"] = (f"{sql_driver}://{db_user}:{db_pass}"
                                                 f"@{db_host}:{db_port}/{db_name}")
