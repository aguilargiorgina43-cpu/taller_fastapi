from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schemas.orden_servicio import OrdenCreate, OrdenUpdate, OrdenOut
from app.services import orden_service

router = APIRouter(prefix="/ordenes", tags=["Ordenes de Servicio"])

@router.get("/", response_model=list[OrdenOut])
def listar(db: Session = Depends(get_db)):
    return orden_service.get_all(db)

@router.get("/{id}", response_model=OrdenOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = orden_service.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return obj

@router.post("/", response_model=OrdenOut)
def crear(data: OrdenCreate, db: Session = Depends(get_db)):
    try:
        return orden_service.create(db, data)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="El vehiculo_id no existe")

@router.put("/{id}", response_model=OrdenOut)
def actualizar(id: int, data: OrdenUpdate, db: Session = Depends(get_db)):
    obj = orden_service.update(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return obj

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = orden_service.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return {"mensaje": "Orden eliminada"}
