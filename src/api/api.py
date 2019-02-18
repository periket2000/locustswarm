from flask import Flask, Blueprint
from werkzeug.contrib.fixers import ProxyFix
import os
from api.restplus import api
from api.blueprints.health_bp import ns as health_namespace

ROOT = os.getenv("API_ROOT", "/api")
# Flask settings
FLASK_DEBUG = False  # Do not use debug mode in production
# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api_', __name__, url_prefix=ROOT)
    api.init_app(blueprint)
    api.add_namespace(health_namespace)
    flask_app.register_blueprint(blueprint)


def app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    initialize_app(app)
    return app
