from typing import List, Type

from sqlalchemy import delete
from sqlalchemy.orm import scoped_session

from app.types.models import ModelInstance


def insert(db_session: scoped_session, items: List[ModelInstance]):
    db_session.add_all(items)
    db_session.commit()


def reset(
    db_session: scoped_session, model: Type[ModelInstance]
):  # Type[V] is the class object
    db_session.execute(delete(model))
    db_session.commit()
