# Asesoria 4 - Semana 1

¡Bienvenidos a la ultima asesoría de la semana 1 en CS2031!🎓 En esta asesoría vamos a construir nuestra propia REST API usando FastAPI, aplicaremos los 5 HTTP Methods del CRUD, Patch, Put, Get, Delete, Post. Reforzaremos conceptos teorios de api y esparemos consoldaur tu aprendizaje para que seas capaz de poder completar el Lab 1.

## 📖 Contexto

Vamos a crear nuestro propio sistema de almacenamiento de datos para los alumnos de CS2031, en el cual podremos agregar, modificar, eliminar y consultar los datos de los alumnos.

## 🚀 Objetivo

El objetivo de esta asesoría es que puedas construir tu propia REST API usando FastAPI, aplicando los 5 HTTP Methods del CRUD, Patch, Put, Get, Delete, Post.

# 🛠️ Funcionalidades Requeridas

1. Crear un nuevo alumno
2. Obtener todos los alumnos
3. Obtener un alumno por su id
4. Actualizar un alumno por su id
5. Eliminar un alumno por su id

# 📋 Requerimientos de implementación

## Codigo Base

Usa esta base de código para implementar tu REST API:

```python
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
```

## ⚙️ Dependencias

Usa el siguiente comando para instalar las dependencias necesarias para el laboratorio:
    
```bash
pip install -r requirements.txt
```

## Correr el servidor

Usa el siguiente comando para correr el servidor:

```bash
uvicorn main:app --reload
```

# 🚀 Consideraciones Finales

Esperamos que esta asesoría te haya ayudado a comprender mejor el funcionamiento de las REST API y FastAPI. Si tienes alguna duda, no dudes en contactar a los profesores o ayudantes del curso. ¡Éxito en el laboratorio!🚀