from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.db import meta, engine

patentes = Table("patentes", meta, 
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("patente", String(7), nullable=False)
)

meta.create_all(engine)