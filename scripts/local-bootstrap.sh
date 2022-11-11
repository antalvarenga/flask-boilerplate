# Create .env

cp envs/.env.sample .env

# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Create virtual environment
python3 -m venv ./.venv

# Install dependencies
poetry install

# Set up git hook scripts
pre-commit install
