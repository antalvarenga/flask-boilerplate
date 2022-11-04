from flask import Response
from flask.testing import FlaskClient
from sqlalchemy.orm import scoped_session

from tests.helpers.asserts import assert_in_response_json, assert_response_code


# create and get should be in the same test because the object returned on create
# is the one generated on the app
def test_create_and_get_user_success(db_session: scoped_session, client: FlaskClient):
    """
    SHOULD return a 201
    FROM a POST request to /admin/v1/users
    and
    SHOULD return a 200
    FROM a GET request to /admin/v1/users/<id>
    """

    response1: Response = client.post(
        "/admin/v1/users", json={"name": "Test"}, content_type="application/json"
    )

    assert_response_code(response1, 201)
    assert_in_response_json(response1, {"name": "Test"})

    user_id = response1.get_json()["id"]

    response2: Response = client.get(
        f"/admin/v1/users/{user_id}", content_type="application/json"
    )

    assert_response_code(response2, 200)
    assert_in_response_json(response2, {"name": "Test", "id": user_id})

    db_session.close()
