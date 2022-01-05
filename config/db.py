#pip install sqlalchemy
#pip install pymysql
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/fastapi_mysql")

meta = MetaData()#La vamos a ocupar en Models
conexion = engine.connect()
