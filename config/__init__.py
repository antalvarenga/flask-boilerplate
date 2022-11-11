import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


# Base configuration and environment variables (secrets)
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
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
