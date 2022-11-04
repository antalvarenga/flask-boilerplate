from typing import TypeVar

from app.stores.database import db

ModelInstance = TypeVar("ModelInstance", bound=db.Model)
