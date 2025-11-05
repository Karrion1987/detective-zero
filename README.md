
# 🕵️‍♂️ Detective Zero

Base del repositorio para un sistema modular de **investigación forense**: ingestión de fuentes, gestión de casos,
evidencias, cadena de custodia, consultas y APIs.

## Stack base
- Python 3.11+
- FastAPI (API y docs /docs)
- PostgreSQL (opcional, via Docker Compose)
- SQLModel / Pydantic
- pytest + ruff + pre-commit
- Docker

## Entorno rápido (sin Docker)
    python -m venv .venv
    .venv\Scripts\activate    # Windows
    pip install -r requirements.txt
    uvicorn detective_zero.app:app --reload

## Docker
    docker compose up --build

API local: http://127.0.0.1:8000  (docs: http://127.0.0.1:8000/docs)

## Estructura
    detective-zero/
      src/detective_zero/
        app.py
        core/
        modules/
          cases/
          evidence/
          ingest/
        routers/
      tests/
      docker/
      requirements.txt
      .env.example

## Scripts útiles
    make format   # lint + format
    make test     # tests
    make run      # uvicorn

## Roadmap breve
- [ ] Conector Telegram OSINT (canales públicos)
- [ ] Ingestión web simple
- [ ] Módulo de OCR (tesseract, opcional)
- [ ] Firma/Verificación de cadena de custodia
- [ ] Panel web
