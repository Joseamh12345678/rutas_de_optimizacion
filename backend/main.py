from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de fruta
class Fruta(BaseModel):
    id: int
    nombre: str

# "Base de datos" en memoria
frutas_db: List[Fruta] = [
    Fruta(id=1, nombre="Manzana"),
    Fruta(id=2, nombre="Pera")
]

# GET – Ver todas las frutas
@app.get("/frutas", response_model=List[Fruta])
def obtener_frutas():
    return frutas_db

# POST – Agregar una nueva fruta
@app.post("/frutas", response_model=Fruta)
def agregar_fruta(fruta: Fruta):
    frutas_db.append(fruta)
    return fruta

# PUT – Actualizar una fruta existente
@app.put("/frutas/{id}", response_model=Fruta)
def actualizar_fruta(id: int, fruta_actualizada: Fruta):
    for i, fruta in enumerate(frutas_db):
        if fruta.id == id:
            frutas_db[i] = fruta_actualizada
            return fruta_actualizada
    raise HTTPException(status_code=404, detail="Fruta no encontrada")

# DELETE – Eliminar una fruta
@app.delete("/frutas/{id}")
def eliminar_fruta(id: int):
    for i, fruta in enumerate(frutas_db):
        if fruta.id == id:
            frutas_db.pop(i)
            return {"mensaje": "Fruta eliminada"}
    raise HTTPException(status_code=404, detail="Fruta no encontrada")