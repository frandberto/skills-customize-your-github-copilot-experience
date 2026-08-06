"""Starter code: Building REST APIs with FastAPI.

Instale as dependencias:
    pip install fastapi uvicorn

Execute localmente:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


# Armazenamento em memoria para a atividade
TASKS: list[Task] = []
NEXT_ID = 1


@app.get("/")
def root() -> dict[str, str]:
    """TODO: Personalize a mensagem de boas-vindas."""
    return {"message": "Welcome to the FastAPI assignment"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    """TODO: Opcional - adicione filtros por completed na query string."""
    return TASKS


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    global NEXT_ID

    task = Task(id=NEXT_ID, **payload.model_dump())
    TASKS.append(task)
    NEXT_ID += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in TASKS:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskCreate) -> Task:
    for i, task in enumerate(TASKS):
        if task.id == task_id:
            updated = Task(id=task_id, **payload.model_dump())
            TASKS[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    for i, task in enumerate(TASKS):
        if task.id == task_id:
            TASKS.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Task not found")
