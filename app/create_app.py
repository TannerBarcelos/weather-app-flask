from flask import Flask
from routes.app_routes import api
import conf # conf is a python module and therefore we can load all its contents into the Flask config using from_object() method
from utils.server_setup import load_conf

# Application factory -> https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/
def create_app() -> Flask:
    app = Flask(__name__)

    load_conf(app, conf)

    # Register root blueprint (wrapper for all routes)
    app.register_blueprint(api, url_prefix='/api')

    return app
