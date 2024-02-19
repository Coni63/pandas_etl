install:
	poetry install
	poetry run pre-commit install

unittest:
	poetry run pytest -v --cov-report term  --cov-report xml:coverage.xml --cov=pandas_etl tests/

run:
	poetry run python -m pandas_etl.main

check:
	poetry run pre-commit run --all-files
