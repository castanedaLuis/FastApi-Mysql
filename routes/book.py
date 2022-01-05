from fastapi import APIRouter, Response, status
from config.db import conexion
from models.book import books #books es la tabla
from schemas.book import Book #Tipo de dato Book

from starlette.status import HTTP_204_NO_CONTENT #Para poder responder el status

book = APIRouter()

#-----------------------------
@book.get("/books", response_model=Book, tags=["books"])
def get_books():
    return conexion.execute(books.select()).fetchall() #Hacemos una consulta a toda la tabla

#-----------------------------
@book.post("/books",response_model=Book, tags=["books"])
def create_book(book:Book):
    new_book={"name": book.name,"autor":book.autor,"descrition":book.descrition,"page":book.page}#para convertirlo en un Diccionario
    result = conexion.execute(books.insert().values(new_book))
    return conexion.execute(books.select().where(books.c.id == result.lastrowid)).first()

#-----------------------------
@book.get("/books/{id_book}",response_model=Book, tags=["books"])
def get_book(id_book:str):
    return conexion.execute(books.select().where(books.c.id == id_book)).first()

#-----------------------------
@book.delete("/books/{id_book}", status_code=status.HTTP_204_NO_CONTENT, tags=["books"])
def delete_book(id_book:str):
    results = conexion.execute(books.delete().where(books.c.id == id_book))
    return Response(status_code=HTTP_204_NO_CONTENT)

#-----------------------------
@book.put("/books/{id_book}",response_model=Book, tags=["books"])
def update_book(id_book:str, book:Book):
    conexion.execute(books.update().values(name = book.name, 
                                                autor = book.autor,
                                                descrition = book.descrition,
                                                page = book.page).
                                                where(books.c.id == id_book))
    return conexion.execute(books.select().where(books.c.id == id_book)).first()




