from typing import Dict

from flask import Response


def assert_response_code(response: Response, code: int):
    try:
        assert response.status_code == code
    except AssertionError as e:
        e.args += (response.status_code, "==", code)
        raise


def assert_in_response_json(response: Response, expected: Dict):
    json: Dict = response.get_json()
    try:
        assert expected.items() <= json.items()
    except AssertionError as e:
        e.args += (expected, "in", json)
        raise
