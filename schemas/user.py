#Nos sirve para crear los Tipos de objetos
from pydantic import BaseModel
from typing import Optional



class User(BaseModel):
    id:Optional[str]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    class Config:
        orm_mode = True
    
