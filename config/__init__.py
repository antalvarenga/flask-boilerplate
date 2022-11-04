# Base configuration and environment variables (secrets)
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Config:
    TESTING = False
    APISPEC_SPEC = APISpec(
        title="Flask boilerplate",
        version="v0.1.0",
        openapi_version="2.0",
        plugins=[MarshmallowPlugin()],
    )
    APISPEC_SWAGGER_URL = "/docs-json/"
    APISPEC_SWAGGER_UI_URL = "/docs/"


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app_root:123456@localhost/flask_app"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app_root:123456@database/flask_app"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://flask_app_root:123456@localhost/flask_app_test"
    )
