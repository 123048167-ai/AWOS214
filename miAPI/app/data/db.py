from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#definimos la URL de la BD
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:123456@postgres:5432/DB_miapi"
)

#2. creamos el motor de conexion 
engine= create_engine(DATABASE_URL)

# creamos gestionador de sesiones
SessionLocal= sessionmaker(
    autocommit= False,
    autoflush= False,
    bind= engine
)