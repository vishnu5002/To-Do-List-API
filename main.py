from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
from datetime import datetime

app = FastAPI(title="To-Do List API")

# Pydantic models for request/response validation
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: str

# Database setup
def init_db():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Helper function to convert DB row to TaskResponse
def row_to_task(row):
    return TaskResponse(
        id=row[0],
        title=row[1],
        description=row[2],
        status=row[3],
        created_at=row[4]
    )

# Endpoints
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
            (task.title, task.description, task.status)
        )
        conn.commit()
        task_id = cursor.lastrowid
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        return row_to_task(cursor.fetchone())

@app.get("/tasks", response_model=List[TaskResponse])
async def get_tasks():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = [row_to_task(row) for row in cursor.fetchall()]
        return tasks

@app.get("/tasks/{id}", response_model=TaskResponse)
async def get_task(id: int):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return row_to_task(row)

@app.put("/tasks/{id}", response_model=TaskResponse)
async def update_task(id: int, task: TaskUpdate):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise HTTPException(status_code=404, detail="Task not found")
        
        update_data = task.dict(exclude_unset=True)
        if update_data:
            query = "UPDATE tasks SET " + ", ".join(f"{k} = ?" for k in update_data.keys()) + " WHERE id = ?"
            values = list(update_data.values()) + [id]
            cursor.execute(query, values)
            conn.commit()
        
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        return row_to_task(cursor.fetchone())

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            raise HTTPException(status_code=404, detail="Task not found")
        cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        conn.commit()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)