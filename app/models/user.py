import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.stores.database import db


class User(Base, db.Model):
    name: Mapped[str] = mapped_column(sa.String(), nullable=False)
