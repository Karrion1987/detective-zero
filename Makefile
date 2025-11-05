
.PHONY: run test format

run:
	uvicorn detective_zero.app:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -q

format:
	ruff check --fix .
