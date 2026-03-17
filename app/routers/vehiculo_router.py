from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schemas.vehiculo import VehiculoCreate, VehiculoUpdate, VehiculoOut
from app.services import vehiculo_service

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

@router.get("/", response_model=list[VehiculoOut])
def listar(db: Session = Depends(get_db)):
    return vehiculo_service.get_all(db)

@router.get("/{id}", response_model=VehiculoOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = vehiculo_service.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return obj

@router.post("/", response_model=VehiculoOut)
def crear(data: VehiculoCreate, db: Session = Depends(get_db)):
    try:
        return vehiculo_service.create(db, data)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="La placa ya está registrada o el cliente no existe")

@router.put("/{id}", response_model=VehiculoOut)
def actualizar(id: int, data: VehiculoUpdate, db: Session = Depends(get_db)):
    obj = vehiculo_service.update(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return obj

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = vehiculo_service.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return {"mensaje": "Vehiculo eliminado"}
