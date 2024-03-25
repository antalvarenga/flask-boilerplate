from unittest.mock import patch

from app.tasks import add


def test_celery_raw_fixtures(celery_app, celery_worker):
    with patch("app.tasks.time.sleep") as mock_sleep:
        result = add.delay(4, 4)

        assert result.get() == 8  # Ensure the result is correct
        mock_sleep.assert_called_with(10)
