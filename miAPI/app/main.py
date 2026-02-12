#importaciones
from fastapi import FastAPI
import asyncio
from typing import Optional

#instancia del servidor
app = FastAPI(
    title="MI PRIMER API",
    description="Esta es la API de jafet uribe",
    version="1.0.0"
    )

#BD ficticia
usuarios=[
    {"id":1,"nombre":"rogelio","edad":21},
    {"id":2,"nombre":"gabo jobs","edad":35},
    {"id":3,"nombre":"isaac","edad":21},
]

#Endpoints
@app.get("/",tags=['Inicio'])
async def root():
    return {"mensaje": "Bienvenido a mi API"}

@app.get("/HolaMundo",tags=['Bienvenida Asincrona'])
async def hola():
    await asyncio.sleep(3)
    return {
        "mensaje": "Hola Mundo FastAPI",
        "estatus":  "200"
        }

@app.get("/v1/usuarios/{id}",tags=['Parametro oblogatorio'])
async def consultaUno(id:int):
    return {"Se encontro usuario": id,
         }

@app.get("/v1/usuarios/",tags=['Parametro Opcional'])
async def consultaTodos(id:Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]== id:
                return {"mensaje":"usuario encontrado","usuario":usuario}
        return {"mensaje":"usuario no encontrado","usuario":id}
    else:
        return {"mensaje":"No se proporciono id"}

