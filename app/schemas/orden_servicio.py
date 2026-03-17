from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class OrdenBase(BaseModel):
    descripcion: str
    fecha: date
    costo: Decimal
    vehiculo_id: int

class OrdenCreate(OrdenBase):
    pass

class OrdenUpdate(OrdenBase):
    pass

class OrdenOut(OrdenBase):
    id: int
    class Config:
        from_attributes = True
