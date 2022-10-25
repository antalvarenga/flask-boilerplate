from sqlalchemy.dialects.postgresql import UUID
from app.stores.database import db
import uuid

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
