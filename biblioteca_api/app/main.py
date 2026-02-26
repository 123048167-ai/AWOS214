from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API Biblioteca Digital",
    description="API básica para gestión de libros y préstamos",
    version="1.0.0"
)


# MODELOS

class Libro(BaseModel):
    id: int = Field(..., example=1)
    nombre: str = Field(..., min_length=3, example="El Principito")
    autor: str = Field(..., min_length=3, example="Antoine de Saint-Exupéry")
    disponible: bool = True



class Prestamo(BaseModel):
    libro_id: int = Field(..., example=1)
    usuario: str = Field(..., min_length=3, example="Jafet")




# BASE DE DATOS FICTICIA


libros: List[Libro] = []
prestamos: List[Prestamo] = []


# ENDPOINTS


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

# LIBROS

@app.get("/libros")
def listar_libros():
    return libros

@app.post("/libros")
def registrar_libro(libro: Libro):
    for l in libros:
        if l.id == libro.id:
            raise HTTPException(status_code=400, detail="El libro ya existe")
    libros.append(libro)
    return libro

@app.get("/libros/{nombre}")
def buscar_libro(nombre: str):
    for libro in libros:
        if libro.nombre.lower() == nombre.lower():
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

#  PRESTAMOS 

@app.post("/prestamos")
def registrar_prestamo(prestamo: Prestamo):
    for libro in libros:
        if libro.id == prestamo.libro_id:
            if not libro.disponible:
                raise HTTPException(status_code=400, detail="Libro no disponible")
            libro.disponible = False
            prestamos.append(prestamo)
            return {"mensaje": "Préstamo registrado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.put("/prestamos/{libro_id}")
def devolver_libro(libro_id: int):
    for libro in libros:
        if libro.id == libro_id:
            libro.disponible = True
            return {"mensaje": "Libro devuelto correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.delete("/prestamos/{libro_id}")
def eliminar_prestamo(libro_id: int):
    global prestamos
    prestamos = [p for p in prestamos if p.libro_id != libro_id]
    return {"mensaje": "Préstamo eliminado correctamente"}