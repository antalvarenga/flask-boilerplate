from flask import Response
from flask.testing import FlaskClient
from sqlalchemy.orm import scoped_session

from tests.fixtures.user import UserFixtureFactory
from tests.helpers.database import insert
from tests.helpers.asserts import assert_response_code

def test_get_user_success(db_session: scoped_session, client: FlaskClient, user_list: UserFixtureFactory):
    """
    SHOULD return a 200
    FROM a GET request to /admin/v1/users/<id>
    """

    users = user_list(1)
    insert(db_session, users)

    response: Response = client.get(f"/admin/v1/users/{users[0].id}", content_type="application/json")

    assert_response_code(response, 200)