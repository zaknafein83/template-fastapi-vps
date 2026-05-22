import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="myapp", version="1.0.0")

# CORS dal valore env (separare con virgole)
origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello", response_class=None)
def hello() -> str:
    return "Hello from myapp"


@app.get("/health")
def health() -> dict:
    return {"status": "UP"}
