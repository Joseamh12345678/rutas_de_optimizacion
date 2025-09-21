from fastapi import APIRouter, HTTPException
from src.models.route_model import UsuarioEntrada, UsuarioSalida
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

usuariosdb: List[UsuarioSalida] = []

@router.post("/", response_model=UsuarioSalida)
def crear_usuario(usuario: UsuarioEntrada):
    if any(u.correo == usuario.correo for u in usuariosdb):
        raise HTTPException(status_code=400, detail="El correo ya existe, intente con otro")
    nuevo_id=len(usuariosdb) + 1
    nuevo_usuario = UsuarioSalida(
        id=nuevo_id,
        nombre=usuario.nombre,
        correo=usuario.correo
    )
    usuariosdb.append(nuevo_usuario)
    return nuevo_usuario

@router.get("/", response_model=List[UsuarioSalida])
def obtener_usuarios():
    return usuariosdb

@router.get("/{id}", response_model=UsuarioSalida)
def obtener_usuario(id: int):
    usuario = next((u for u in usuariosdb if u.id == id), None)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario no existente o no encontrado")

