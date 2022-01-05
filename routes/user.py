from fastapi import APIRouter, Response, status
from config.db import conexion
from models.user import users #users es la tabla
from schemas.user import User #Importamos la clase que se creo para el tipo de dato
from cryptography.fernet import Fernet #Para encriptar la contraseña
from starlette.status import HTTP_204_NO_CONTENT #Para poder responder el status

key = Fernet.generate_key()#Hacer la encriptacion
f = Fernet(key)
user = APIRouter()

#-----------------------------
@user.get("/users", response_model=User, tags=["users"])
def get_users():
    return conexion.execute(users.select()).fetchall() #Hacemos una consulta a toda la tabla

#-----------------------------
@user.post("/users",response_model=User, tags=["users"])
def create_user(user:User):
    new_user={"name": user.name,"email":user.email}#para convertirlo en un Diccionario
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conexion.execute(users.insert().values(new_user))
    return conexion.execute(users.select().where(users.c.id == result.lastrowid)).first()

#-----------------------------
@user.get("/users/{id_user}",response_model=User, tags=["users"])
def get_user(id_user:str):
    return conexion.execute(users.select().where(users.c.id == id_user)).first()

#-----------------------------
@user.delete("/users/{id_user}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id_user:str):
    results = conexion.execute(users.delete().where(users.c.id == id_user))
    return Response(status_code=HTTP_204_NO_CONTENT)

#-----------------------------
@user.put("/users/{id_user}",response_model=User, tags=["users"])
def update_user(id_user:str, user:User):
    conexion.execute(users.update().values(name = user.name, 
                                                email = user.email,
                                                password = f.encrypt(user.password.encode("utf-8"))).
                                                where(users.c.id == id_user))
    return conexion.execute(users.select().where(users.c.id == id_user)).first()




