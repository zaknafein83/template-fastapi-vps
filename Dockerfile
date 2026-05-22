FROM python:3.12-slim AS base

# Niente cache pip + niente bytecode pyc per immagini piccole
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Installa solo le dipendenze prima (per cache layer)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia il codice
COPY app ./app

# User non-root
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
