from sqlalchemy.orm import Session
from app.repositories import cliente_repo
from app.schemas.cliente import ClienteCreate, ClienteUpdate

def get_all(db: Session):
    return cliente_repo.get_all(db)

def get_by_id(db: Session, id: int):
    return cliente_repo.get_by_id(db, id)

def create(db: Session, data: ClienteCreate):
    return cliente_repo.create(db, data.dict())

def update(db: Session, id: int, data: ClienteUpdate):
    return cliente_repo.update(db, id, data.dict())

def delete(db: Session, id: int):
    return cliente_repo.delete(db, id)
