from sqlalchemy.orm import Session
from app.repositories import vehiculo_repo
from app.schemas.vehiculo import VehiculoCreate, VehiculoUpdate

def get_all(db: Session):
    return vehiculo_repo.get_all(db)

def get_by_id(db: Session, id: int):
    return vehiculo_repo.get_by_id(db, id)

def create(db: Session, data: VehiculoCreate):
    return vehiculo_repo.create(db, data.dict())

def update(db: Session, id: int, data: VehiculoUpdate):
    return vehiculo_repo.update(db, id, data.dict())

def delete(db: Session, id: int):
    return vehiculo_repo.delete(db, id)
