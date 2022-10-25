from typing import Final, Generic, Optional, TypeVar, cast
# from flask_sqlalchemy import BaseQuery, Model
from app.stores.database import db

M = TypeVar("M", bound=db.Model)

class Base(Generic[M]):
    _model = M

    def get_by_id(self, id) -> str:
        # query = self._query()
        return "laskdn"

    def create(self, **data):
        record: Final = self._model(**data)
        db.session.add(record)
        db.session.commit()

    
    # def _query(self):
    #     return cast(BaseQuery, self._model.query)