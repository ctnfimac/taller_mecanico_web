from dataclasses import dataclass
from datetime import datetime


@dataclass
class WorkShop:
    id:int 
    email:str 
    password:str
    activated:bool 
    created_at:datetime
    updated_at:datetime 