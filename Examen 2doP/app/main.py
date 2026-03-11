from fastapi import fastApi, HTTPExeption
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API Sistema de Tickets de Soporte Tecnico",
    description="API básica para gestiónar tickets",
    version="1.0.0"
)

# modelo
class Ticket(BaseModel):
    id: int = Field(..., example=1)
    nombre: str = Field(..., min_length=3, example="Jafet")
    descripcion: str = Field(..., min_length=3, example="Necesita poder tener un almacen completo donde los datos de sus administradores aparezcan completos")
    prioridad : Field(..., min_length=3, example="media")
    disponible: bool = True


class Ticket(BaseModel):
    id: int = Field(..., example=2)
    nombre: str = Field(..., min_length=3, example="Isaac")
    descripcion: str = Field(..., min_length=3, example="Requiere hacer un listado de horarios de entrada de cada uno de los integrantes, pertenecientes a su aula")
    prioridad : Field(..., min_length=3, example="baja")
    disponible: bool = True



# BASE DE DATOS FICTICIA


Tickets: List[Tickets] = []
tickets: List[tickets] = []




@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

# Tickets

@app.get("/Tickets")
def listar_Ticket():
    return 

@app.post("/Tickets")
def registrar_Tickets(T: tickets):
    for l in Tickets:
        if l.id == tickets.id:
            raise HTTPException(status_code=400, detail="El Ticket tiene un estado: ")
    tickets.append(tickets)
    return tickets

@app.get("/Tickets/{nombre}")
def buscar_Tickets(nombre: str):
    for tickets in tickets:
        if Ticket.nombre.lower() == nombre.lower():
            return Ticket
    raise HTTPException(status_code=404, detail="ticket no encontrado")


# consulta de tickets


