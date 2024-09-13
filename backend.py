# backend.py

from fastapi import FastAPI

app = FastAPI()  # This is the app that Uvicorn is looking for

@app.get("/")
def read_root():
    return {"message": "Hello World"}
