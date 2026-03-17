from pydantic import BaseModel

class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    anio: int
    placa: str
    cliente_id: int

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(VehiculoBase):
    pass

class VehiculoOut(VehiculoBase):
    id: int
    class Config:
        from_attributes = True
