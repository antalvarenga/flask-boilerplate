import os

# Base configuration and environment variables (secrets)
class Config:
    TESTING = False

class LocalConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app_root:123456@localhost/flask_app"


