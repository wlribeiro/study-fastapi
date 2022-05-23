from typing import List, Dict, Any, Optional
from pydantic import BaseModel

from data import  StatusOptions

class ToDoModelIten(BaseModel):
    title: str
    status: Optional[StatusOptions]

class ResponseModelItem(ToDoModelIten):
    id: int