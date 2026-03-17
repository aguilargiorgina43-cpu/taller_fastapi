from fastapi import FastAPI
from app.database import Base, engine
from app.models import cliente, vehiculo, orden_servicio
from app.routers import cliente_router, vehiculo_router, orden_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Taller de Servicio - CRUD FastAPI")

app.include_router(cliente_router.router)
app.include_router(vehiculo_router.router)
app.include_router(orden_router.router)
