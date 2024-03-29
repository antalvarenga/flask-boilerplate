from flask import Flask
from flask_apispec import FlaskApiSpec
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api import v1 as admin_v1
from config import database


def create_app(env="local"):
    app = Flask(__name__)

    print(env)
    if env == "prod":
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
        app.config.from_object("config.ProductionConfig")
    if env == "local":
        app.config.from_object("config.LocalConfig")
    if env == "testing":
        app.config.from_object("config.TestingConfig")

    docs: FlaskApiSpec = FlaskApiSpec()

    docs.init_app(app)
    admin_v1.init_app(app, docs)
    database.init_app(app)
    return app
