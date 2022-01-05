from sys import version
from fastapi import FastAPI
from routes.user import user
from routes.book import book


app = FastAPI(
    title = "Seguna API MySQL",
    description="Utlizamos la herramienta sqlalchemy para conectar la base de datos",
    version="1.0.0"
)

app.include_router(user) #Para incluir las routas externas
app.include_router(book)

