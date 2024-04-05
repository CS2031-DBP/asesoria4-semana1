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

@app.get("/")
def read_root():
    return "Bienvenido a la API de estudiantes"

@app.get("/estudiantes")
def read_estudiantes():
    return estudiantes

@app.get("/estudiantes/{estudiante_id}")
def read_estudiante(estudiante_id: UUID):
    for estudiante in estudiantes:
        if estudiante.id == estudiante_id:
            return estudiante
    return "Estudiante no encontrado"

@app.post("/estudiantes")
def create_estudiante(estudiante: Estudiantes):
    estudiante.id = uuid4()
    estudiantes.append(estudiante)
    return estudiante

@app.put("/estudiantes/{estudiante_id}")
def update_estudiante(estudiante_id: UUID, estudiante: Estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i].id == estudiante_id:
            estudiantes[i] = estudiante
            return estudiante
    return "Estudiante no encontrado"

@app.patch("/estudiantes/{estudiante_id}")
def update_estudiante(estudiante_id: UUID, estudiante: Estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i].id == estudiante_id:
            if estudiante.nombre:
                estudiantes[i].nombre = estudiante.nombre
            if estudiante.edad:
                estudiantes[i].edad = estudiante.edad
            if estudiante.correo:
                estudiantes[i].correo = estudiante.correo
            return estudiantes[i]
    return "Estudiante no encontrado"

@app.delete("/estudiantes/{estudiante_id}")
def delete_estudiante(estudiante_id: UUID):
    for i in range(len(estudiantes)):
        if estudiantes[i].id == estudiante_id:
            estudiante = estudiantes[i]
            del estudiantes[i]
            return estudiante
    return "Estudiante no encontrado"