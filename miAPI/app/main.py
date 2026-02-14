#importaciones
from fastapi import FastAPI, status, HTTPException
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

@app.get("/v1/parametroOb/{id}",tags=['Parametro oblogatorio'])
async def consultaUno(id:int):
    return {"Se encontro usuario": id,
         }

@app.get("/v1/parametroOp/",tags=['Parametro Opcional'])
async def consultaTodos(id:Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]== id:
                return {"mensaje":"usuario encontrado","usuario":usuario}
        return {"mensaje":"usuario no encontrado","usuario":id}
    else:
        return {"mensaje":"No se proporciono id"}



@app.get("/v1/usuarios/",tags=['CRUD HTTP'])
async def leer_uruarios():
    return{
        "status":"200",
        "total": len(usuarios),
        "usuarios":usuarios
    }

@app.post("/v1/usuarios/",tags=['CRUD HTTP'],status_code=status.HTTP_201_CREATED)
async def crear_uruario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario Agregado",
        "Usuario":usuario
    }


@app.put("/v1/usuarios/",tags=['CRUD HTTP'],status_code=status.HTTP_200_OK)
async def actualozar_usuario(id:int,usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario Agregado",
        "Usuario":usuario
    }



