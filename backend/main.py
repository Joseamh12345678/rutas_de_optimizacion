from fastapi import FastAPI
from src.routes import users

app = FastAPI(
    title="Sistema de Optimizacion de Rutas",
    description="API para gestion de usuarios y rutas",
    version="1.0.0"
)

app.include_router(users.router)