#sqlalchemy Te permite crear la stablas desde python
from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta, engine




books = Table("books",meta, Column("id", Integer, primary_key=True),
                            Column("name", String(255)),
                            Column("autor", String(255)),
                            Column("descrition", String(255)),
                            Column("page",Integer))

#engine es el que se conecta a la DB
meta.create_all(engine)