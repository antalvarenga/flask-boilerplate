# Fixtures in conftest.py will be available to every test inside the same folder

from typing import Final
from flask import Flask
import pytest
from app import create_app


pytest_plugins = ["tests.fixtures"]

@pytest.fixture()
def app():
    app: Final[Flask] = create_app(env="testing")

    with app.app_context():
        yield app


@pytest.fixture()
def client(app: Flask):
    with app.test_client() as client:
        yield client