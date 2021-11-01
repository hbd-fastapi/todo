from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    name: str 
    due_date: str
    description: str


app = FastAPI(title="Todo API")


# Create, read, update, delete

db = []

@app.get("/")
async def home():
    return {"Hello": "World"}


@app.post('/todo/')
async def create_todo(todo: Todo):
    db.append(todo)
    return todo


@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return db


@app.get('/todo/{id}')
async def get_todo(id: int):
    try:    
        return db[id]
    except HTTPException:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
    try:
        db[id] = todo
        return db[id]
    except HTTPException:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete("/todo/{id}")
async def delete_todo(id: int):
    try:
        obj = db.pop(id)
        return obj
    except HTTPException:
        raise HTTPException(status_code=404, detail="Todo Not Found")
