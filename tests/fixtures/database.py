import pytest
from flask import Flask
from flask_migrate import upgrade
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session

from app.stores.database import db


@pytest.fixture
def database(app: Flask):
    upgrade()

    yield db

    db.engine.execute("DROP TABLE alembic_version")
    db.session.close()
    db.drop_all()


@pytest.fixture
def db_session(database: SQLAlchemy) -> scoped_session:
    return database.session
