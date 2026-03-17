from sqlalchemy import Column, Integer, Text, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OrdenServicio(Base):
    __tablename__ = "orden_servicio"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(Text, nullable=False)
    fecha = Column(Date, nullable=False)
    costo = Column(Numeric(10, 2), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"), nullable=False)
    vehiculo = relationship("Vehiculo", back_populates="ordenes")
