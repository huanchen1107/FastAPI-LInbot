from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World 這是test"}

@app.get("/hello")
def read_root2():
    return {"Hello2": "222 World 這是test"}
