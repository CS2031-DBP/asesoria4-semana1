from pydantic import BaseModel
from typing import Optional
from uuid import uuid4, UUID
from fastapi import FastAPI

app = FastAPI()

# Modelo para los estudiantes
class Estudiantes(BaseModel):
    id: Optional[UUID] = None
    nombre: Optional[str] = None
    edad: Optional[int] = None
    correo: Optional[str] = None

# Lista de estudiantes
estudiantes = [
    Estudiantes(id=uuid4(), nombre="Juan Lopez", edad=20, correo="juan.lopez@utec.edu.pe"),
    Estudiantes(id=uuid4(), nombre="Maria Perez", edad=22, correo="maria.perez@utec.edu.pe")
]