from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.get("/search")
def search_items(category: Optional[str] = None, limit: int = 10):
    return {"category": category, "limit": limit}

@app.post("/users/")
def create_user(user: User):
    return {
        "message": f"User {user.name} created successfully.",
        "user": user.dict(),
    }

# Run locally with:
# uvicorn starter-code:app --reload
# Example requests:
# GET http://127.0.0.1:8000/
# GET http://127.0.0.1:8000/items/1?q=test
# POST http://127.0.0.1:8000/users/ with JSON body
