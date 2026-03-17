from sqlalchemy.orm import Session
from app.repositories import orden_repo
from app.schemas.orden_servicio import OrdenCreate, OrdenUpdate

def get_all(db: Session):
    return orden_repo.get_all(db)

def get_by_id(db: Session, id: int):
    return orden_repo.get_by_id(db, id)

def create(db: Session, data: OrdenCreate):
    return orden_repo.create(db, data.dict())

def update(db: Session, id: int, data: OrdenUpdate):
    return orden_repo.update(db, id, data.dict())

def delete(db: Session, id: int):
    return orden_repo.delete(db, id)
