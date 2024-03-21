from dotenv import load_dotenv

load_dotenv()
from app import create_app  # noqa

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
