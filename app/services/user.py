from app.models.user import User
from app.services.base import Base


class UserService(Base[User]):
    def __init__(self):
        self._model = User
