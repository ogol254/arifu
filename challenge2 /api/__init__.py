from flask import Flask, Blueprint, request, make_response, jsonify
import json


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    # app.wsgi_app = ProxyFix(app.wsgi_app)

    # local imports
    from .v1 import version_one as v1

    app.register_blueprint(v1)

    return app


app = create_app()
