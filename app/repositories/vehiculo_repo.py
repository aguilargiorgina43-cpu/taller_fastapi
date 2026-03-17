from sqlalchemy.orm import Session
from app.models.vehiculo import Vehiculo

def get_all(db: Session):
    return db.query(Vehiculo).all()

def get_by_id(db: Session, vid: int):
    return db.query(Vehiculo).filter(Vehiculo.id == vid).first()

def create(db: Session, data: dict):
    obj = Vehiculo(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, vid: int, data: dict):
    obj = get_by_id(db, vid)
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete(db: Session, vid: int):
    obj = get_by_id(db, vid)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
