from typing import List, Dict, Any, Optional, Union
from enum import Enum


class StatusOptions(str, Enum):
    to_do = "A Fazer"
    doing = "Fazendo"
    done = "Feito"


Item = Dict[str, Union[int, str, StatusOptions]]


class ToDo():

    to_do: List[Item] = [
    {"id": 1, "title": "Fazer live", "status": StatusOptions.to_do},
    {"id": 2,"title": "Ligar streamming", "status": StatusOptions.to_do},
    {"id": 3,"title": "Pentear o cabelo", "status": StatusOptions.to_do}
    ]

    actual_id = 3

    def listar(self):
        return self.to_do
    
    def insert(self, item: Item) -> Item:
        self.actual_id += 1
        item["id"] = self.actual_id
        self.to_do.append(item)
        return item
    
    def get_item(self, item_id: int) -> Item :
        item = filter(lambda x: x["id"] == item_id, self.to_do)
        return list(item)[0]
    
    def filter_item(self, status: StatusOptions) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.to_do))
