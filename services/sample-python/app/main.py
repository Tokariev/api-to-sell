import os

from fastapi import FastAPI

app = FastAPI(
    title="Sample Python API",
    description="Sample API service for RapidAPI",
    version="1.0.0",
    root_path=os.getenv("ROOT_PATH", ""),
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello from Sample Python API"}
