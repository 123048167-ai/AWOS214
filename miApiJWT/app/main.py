# Importaciones
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional, List
from pydantic import BaseModel


# CONFIGURACIÓN JWT


SECRET_KEY = "clave_super_secreta_jafeturibe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


# OAuth2


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Encriptación de contraseña


pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


# Usuario simulado


fake_user = {
    "username": "jafeturibe",
    "hashed_password": pwd_context.hash("123456")
}


# MODELOS


class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str

class UsuarioCreate(BaseModel):
    nombre: str
    correo: str

class Token(BaseModel):
    access_token: str
    token_type: str


# BASE DE DATOS SIMULADA


usuarios = [
    {"id":1,"nombre":"Juan","correo":"juan@gmail.com"},
    {"id":2,"nombre":"Gabriel","correo":"gabriel@gmail.com"},
    {"id":3,"nombre":"Isaac","correo":"isaac@gmail.com"}
]


# FUNCIONES DE SEGURIDAD


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    if username != fake_user["username"]:
        return False
    if not verify_password(password, fake_user["hashed_password"]):
        return False
    return fake_user


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )


# APP


app = FastAPI(
    title="Mi primer API",
    description="Jafet uribe uribe",
    version="2.0.0"
)


# LOGIN


@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )

    access_token = create_access_token(
        data={
            "sub": user["username"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ENDPOINTS


@app.get("/")
def bienvenida():
    return {"mensaje": "Bienvenido a la API"}


@app.get("/HolaMundo")
async def hola():
    return {"mensaje": "Hola mundo asincrono"}


@app.get("/v1/parametroOp/{id}")
def parametro_obligatorio(id: int):
    return {"id": id}


@app.get("/v1/parametroOp/")
def parametro_opcional(nombre: Optional[str] = None):
    return {"nombre": nombre}


# CRUD USUARIOS


@app.get("/v1/usuarios/")
def leer_usuarios():
    return usuarios


@app.post("/v1/usuarios/")
def crear_usuario(usuario: UsuarioCreate):

    nuevo = {
        "id": len(usuarios) + 1,
        "nombre": usuario.nombre,
        "correo": usuario.correo
    }

    usuarios.append(nuevo)

    return nuevo


# ENDPOINT PROTEGIDO PUT


@app.put("/v1/usuarios/{id_buscado}")
def actualizar_usuario(
    id_buscado: int,
    usuario: UsuarioCreate,
    token: str = Depends(oauth2_scheme)
):

    verify_token(token)

    for u in usuarios:

        if u["id"] == id_buscado:

            u["nombre"] = usuario.nombre
            u["correo"] = usuario.correo

            return u

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# ENDPOINT PROTEGIDO DELETE


@app.delete("/v1/usuarios/{id}")
def eliminar_usuario(
    id: int,
    token: str = Depends(oauth2_scheme)
):

    verify_token(token)

    for u in usuarios:

        if u["id"] == id:

            usuarios.remove(u)

            return {
                "mensaje": "Usuario eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )