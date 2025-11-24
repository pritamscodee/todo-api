from pydantic import BaseModel

class input_tasks(BaseModel):
    task: str
    is_completed: bool

class show_tasks(BaseModel):
    id: int
    task: str
    is_completed: bool
