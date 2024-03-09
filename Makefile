install:
	poetry install
	poetry run pre-commit install

unittest:
	poetry run pytest --cov-report term  --cov-report xml:coverage.xml --cov=pandas_etl tests/

run:
	poetry run python -m pandas_etl.main

check:
	poetry run pre-commit run --all-files

ui:
	cd pandas-etl-ui && ng serve -o
