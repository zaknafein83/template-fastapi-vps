# template-fastapi-vps

Template GitHub per backend FastAPI + Python 3.12, deployato via Docker su VPS `zaknafein.ovh`.

## Stack

| Layer | Tecnologia |
|---|---|
| Framework | FastAPI 0.115 |
| Server | Uvicorn |
| Python | 3.12 |
| ORM | SQLAlchemy 2 + psycopg 3 (Postgres) — opzionale |
| Migrazioni | Alembic — opzionale |
| Test | pytest + httpx |
| Container | Docker (python:3.12-slim, user non-root) |

## Endpoint

- `GET /hello` → "Hello from myapp"
- `GET /health` → `{"status":"UP"}`
- `GET /docs` → Swagger UI auto-generata
- `GET /redoc` → ReDoc auto-generato

## Sviluppo locale

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
# → http://localhost:8000/hello
# → http://localhost:8000/docs
```

## Test

```bash
pytest
```

## Attivare il DB

Il template `app/main.py` non si collega a Postgres di default (per restare runnable senza container). Quando ti serve:

1. Crea `app/db.py` con un engine SQLAlchemy che usa `os.getenv("DATABASE_URL")`
2. Crea modelli in `app/models/`
3. Aggiungi `Depends(get_db)` nei tuoi router
4. Inizializza Alembic per le migrazioni: `alembic init alembic`

Per MongoDB: scambia in `requirements.txt` il blocco Postgres con motor/pymongo (commenti già presenti).

## Init

```bash
./init-rename.sh <nome-progetto>
```

## Licenza

[MIT](LICENSE)
