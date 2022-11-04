import logging
import os

from config import Config
from flask import Flask
from src.database import database
from src.routes.county_state import pjm_data_app
from utils.log import setup_logger


def create_app() -> Flask:
    """Callable that builds a flask app from config file

    Returns:
        Flask: the flask app
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)

    app.register_blueprint(pjm_data_app)
    root_logger.info("Flask app initialized")
    return app

root_path = str(os.path.abspath(os.path.join(__file__,os.pardir)))
print(root_path)
log_path = root_path+Config.LOG_PATH
root_logger = setup_logger(log_path)
appplication = create_app()
if __name__ == "__main__":
    appplication.run(host="0.0.0.0", port=5000, debug=True)
