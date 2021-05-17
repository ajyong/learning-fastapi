from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def item_detail(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
