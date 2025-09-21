#importar las librerias necesarias
from pydantic import BaseModel, Field
from typing import List, Optional

class UsuarioEntrada(BaseModel):
    nombre: str
    correo: str
    contrasena: str = Field(min_lenght=8, max_lenght=15)

class UsuarioSalida(BaseModel):
    id: int
    nombre: str
    correo: str