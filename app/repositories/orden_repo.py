from sqlalchemy.orm import Session
from app.models.orden_servicio import OrdenServicio

def get_all(db: Session):
    return db.query(OrdenServicio).all()

def get_by_id(db: Session, oid: int):
    return db.query(OrdenServicio).filter(OrdenServicio.id == oid).first()

def create(db: Session, data: dict):
    obj = OrdenServicio(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, oid: int, data: dict):
    obj = get_by_id(db, oid)
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete(db: Session, oid: int):
    obj = get_by_id(db, oid)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
