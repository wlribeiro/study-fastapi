from fastapi import APIRouter
from typing import List, Dict, Any, Optional
from models import ToDoModelIten, ResponseModelItem
from data import ToDo, StatusOptions

router = APIRouter()
todo = ToDo()

@router.get("/", response_model=List[ResponseModelItem])
def to_do_list(status: StatusOptions = None):

    if status is not None:
        return todo.filter_item(status=status) 
    return todo.listar()

@router.post("/", response_model=ToDoModelIten, status_code=201)
def insert_to_do(item: ToDoModelIten):
    return todo.insert(item.dict())

@router.post("/{to_do_id}", response_model=ResponseModelItem)
def get_item_to_do(to_do_id: int):
    return todo.get_item(to_do_id)