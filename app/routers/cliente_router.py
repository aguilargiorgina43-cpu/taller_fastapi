from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteOut
from app.services import cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=list[ClienteOut])
def listar(db: Session = Depends(get_db)):
    return cliente_service.get_all(db)

@router.get("/{id}", response_model=ClienteOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = cliente_service.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return obj

@router.post("/", response_model=ClienteOut)
def crear(data: ClienteCreate, db: Session = Depends(get_db)):
    try:
        return cliente_service.create(db, data)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

@router.put("/{id}", response_model=ClienteOut)
def actualizar(id: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    obj = cliente_service.update(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return obj

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = cliente_service.delete(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"mensaje": "Cliente eliminado"}
