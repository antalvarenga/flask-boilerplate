source .venv/bin/activate

poetry install

poetry run flask --debug run
