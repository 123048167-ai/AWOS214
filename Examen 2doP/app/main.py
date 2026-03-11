from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

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





# Modelo de validación pydantic
class usuario_create(BaseModel):
    id: int = Field(..., gt=0, description="Identificador de usuario")
    nombre: str = Field(..., min_length=3, max_length=50, json_schema_extra={"example": "soporte"})
    edad: int = Field(..., ge=1, le=123, description="Edad valida entre 1 - 123")


# Seguridad
security = HTTPBasic()

def verificar_Peticion(credenciales: HTTPBasicCredentials = Depends(security)):
    userAuth = secrets.compare_digest(credenciales.username, "soporte")
    passAuth = secrets.compare_digest(credenciales.password, "4321")

    if not (userAuth and passAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no Autorizadas"
        )
    return credenciales.username


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

@app.post("/Tickets")
def registrar_prestamo(prestamo: Ticket):
    for Ticket in Ticket:
        if tickets.id == prestamo.ticket_id:
            if not Ticket.disponible:
                raise HTTPException(status_code=400, detail="El ticket esta en estado pendiente")
            Ticket.disponible = False
            tickets.append(Ticket)
            return {"mensaje": "Ticket registrado "}
    raise HTTPException(status_code=404, detail="Ticket no encontrado")
