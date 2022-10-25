from typing import Callable, List
from uuid import uuid4

import pytest
from app.models.user import User

UserFixtureFactory = Callable[[int], List[User]]

def __user_list(count: int) -> List[User]:
    users: List = []
    for i in range(1, count + 1):
        user = User(id=str(uuid4()), name=f"User {i}")
        users.append(user)
    
    return users


@pytest.fixture
def user_list() -> UserFixtureFactory:
    def _list(count: int) -> List[User]:
        return __user_list(count)

    return _list