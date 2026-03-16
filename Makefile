install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

coverage:
	pytest --cov=app --cov-report=term-missing

lint:
	ruff check .
