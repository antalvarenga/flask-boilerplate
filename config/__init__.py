# Base configuration and environment variables (secrets)
class Config:
    TESTING = False


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app_root:123456@localhost/flask_app"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://flask_app_root:123456@localhost/flask_app_test"
    )
