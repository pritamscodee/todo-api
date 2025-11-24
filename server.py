from fastapi import FastAPI
from schemas import show_tasks,input_tasks
from typing import List 
from crud import create_task,read_task,update_task,delete_task

app=FastAPI()

@app.post('/post')
def creating_task(input:input_tasks):
    user_id=create_task(input.task,input.is_completed)
    return user_id








@app.get('/get',response_model=List[show_tasks])
def get_task( ):
   rows = read_task()
   return [show_tasks(id=row[0],task=row[1],is_completed=row[2]) for row in rows]

@app.put('/update/{id}',response_model=show_tasks)
def updating_task(task:input_tasks,id:int):
    updated= update_task(task.task,task.is_completed,id=id)
    return updated






