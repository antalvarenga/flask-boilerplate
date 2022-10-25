from app.models.user import User
from app.services.base import Base


class UserService(Base[User]):
    def get_by_id(self, id):
        return {"name": "admin"}
