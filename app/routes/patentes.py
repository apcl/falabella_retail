from fastapi import APIRouter
from ..config.db import conn
from ..models.patente import patentes

patente = APIRouter()

@patente.get("/PatenteById/{id}")
def PatenteById(id:int):
    try:
        res = conn.execute(patentes.select().where(patentes.c.id == id)).first()["patente"]
        return res
    except:
        return("Registro no encontrado.")

@patente.get("/IdByPatente/{patente}")
def IdByPatente(patente:str):
    try:
        res = conn.execute(patentes.select().where(patentes.c.patente == patente)).first()["id"]
        return res
    except:
        return("Registro no encontrado.")
    

