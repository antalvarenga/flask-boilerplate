from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class Base:
    """Base class for database models"""

    id: Mapped[int] = mapped_column(sa.BIGINT(), primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        sa.TIMESTAMP(timezone=True), onupdate=func.now()
    )
