#importaciones
from fastapi import FastAPI
import asyncio

#instancia del servidor
app = FastAPI()

#Endpoints
@app.get("/")
async def root():
    return {"mensaje": "Bienvenido a mi API"}

@app.get("/HolaMundo")
async def hola():
    await asyncio.sleep(4)
    return {
        "mensaje": "Hola Mundo FastAPI",
        "mensaje": "Hola 200"
        }
