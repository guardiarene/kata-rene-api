# kata-rene-api

![CI Pipeline](https://github.com/guardiarene/kata-rene-api/actions/workflows/ci.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=guardiarene_kata-rene-api&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=guardiarene_kata-rene-api)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=guardiarene_kata-rene-api&metric=coverage)](https://sonarcloud.io/summary/new_code?id=guardiarene_kata-rene-api)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg)](https://fastapi.tiangolo.com/)

REST API built with FastAPI that exposes three Python katas as production-ready endpoints,
featuring async SQLite persistence, full test coverage, and a complete CI/CD pipeline.

---

## Overview

Part of the EPAM DevOps Specialization program.

### Katas implemented

| Kata       | Endpoint                     | Description                                     |
|------------|------------------------------|-------------------------------------------------|
| Dictionary | `POST/GET /dictionary/entry` | Add and look up words with persistence          |
| Shopping   | `POST /shopping/total`       | Calculate total cost with tax                   |
| Nth Letter | `POST /nth-letter/build`     | Build a word from nth letter of each input word |

---

## Architecture

```
app/
├── routers/        # HTTP layer — endpoints, status codes, request/response
├── services/       # Business logic — pure Python, no HTTP dependencies  
├── models/         # SQLAlchemy ORM models
├── schemas/        # Pydantic v2 request/response contracts
└── db/             # Async engine, session factory, Base
```

**Design principle:** Business logic in `services/` is completely decoupled from HTTP. Services test independently
without a server, and the framework is swappable without changing logic.

---

## Tech Stack

| Layer        | Technology                      |
|--------------|---------------------------------|
| Framework    | FastAPI + Uvicorn               |
| Database     | SQLite + SQLAlchemy 2.0 (async) |
| Validation   | Pydantic v2                     |
| Testing      | pytest + pytest-asyncio + httpx |
| Linting      | Ruff                            |
| Packaging    | uv                              |
| Container    | Docker (multi-stage build)      |
| CI/CD        | GitHub Actions                  |
| Code Quality | SonarCloud                      |

---

## Getting started

### With Docker (recommended)

```bash
git clone https://github.com/guardiarene/kata-rene-api.git
cd kata-rene-api
docker compose up
```

API available at `http://localhost:8000`

### With local development

```bash
git clone https://github.com/guardiarene/kata-rene-api.git
cd kata-rene-api

# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create venv and install dependencies
uv sync --all-groups

# Activate venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# Run
uvicorn app.main:app --reload
```

---

## API Documentation

Interactive documentation available at:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Endpoints

#### Health

```bash
curl http://localhost:8000/health
```

```json
{
  "status": "ok",
  "app": "Kata Rene API",
  "version": "0.1.0"
}
```

#### Dictionary — Add Entry

```bash
curl -X POST http://localhost:8000/dictionary/entry \
  -H "Content-Type: application/json" \
  -d '{"word":"Apple","definition":"A fruit that grows on trees"}'
```

```json
{
  "word": "apple",
  "definition": "A fruit that grows on trees"
}
```

#### Dictionary — Get Entry

```bash
curl http://localhost:8000/dictionary/entry/apple
```

```json
{
  "word": "apple",
  "definition": "A fruit that grows on trees"
}
```

#### Shopping — Calculate Total

```bash
curl -X POST http://localhost:8000/shopping/total \
  -H "Content-Type: application/json" \
  -d '{"costs":{"socks":5,"shoes":60},"items":["socks","shoes"],"tax":0.09}'
```

```json
{
  "total": 70.85
}
```

#### Nth Letter — Build Word

```bash
curl -X POST http://localhost:8000/nth-letter/build \
  -H "Content-Type: application/json" \
  -d '{"words":["yoda","best","has"]}'
```

```json
{
  "result": "yes"
}
```

---

## Running Tests

```bash
pytest                              # All tests with coverage
pytest tests/test_dictionary.py -v  # Specific file
pytest --no-cov                     # Without coverage (faster)
```

Coverage threshold: **80%** (pipeline fails if below).

---

## CI/CD Pipeline

Every push to `main` triggers: **lint** (Ruff) → **test** (pytest + coverage) → **sonar** & **docker** (parallel).

Sequential execution with `needs:` dependencies ensures fail-fast: if lint fails, tests don't run; if tests fail,
neither SonarCloud nor Docker build proceed.

---
