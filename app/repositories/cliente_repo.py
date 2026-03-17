from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def get_all(db: Session):
    return db.query(Cliente).all()

def get_by_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def create(db: Session, data: dict):
    obj = Cliente(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, cliente_id: int, data: dict):
    obj = get_by_id(db, cliente_id)
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete(db: Session, cliente_id: int):
    obj = get_by_id(db, cliente_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
