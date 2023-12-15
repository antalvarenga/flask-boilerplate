import pytest
from flask import Flask
from flask_migrate import upgrade
from sqlalchemy.orm import scoped_session

from app.stores.database import db


@pytest.fixture(scope="session", autouse=True)
def database(app_session: Flask):
    upgrade()

    yield db

    with db.engine.begin() as conn:
        conn.exec_driver_sql("DROP TABLE alembic_version")

    db.session.close()
    db.drop_all()


@pytest.fixture
def db_session() -> scoped_session:
    return db.session
