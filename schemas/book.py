#Nos sirve para crear los Tipos de objetos
from pydantic import BaseModel
from typing import Optional



class Book(BaseModel):
    id:Optional[str]
    name:Optional[str]
    autor:Optional[str]
    descrition:Optional[str]
    page: Optional[str]
    class Config:
        orm_mode = True