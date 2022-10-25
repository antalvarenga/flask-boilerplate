from flask import Response

def assert_response_code(response: Response, code: int):
    try:
        assert response.status_code == code
    except AssertionError as e:
        e.args += (response.status_code, "==", code)
        raise