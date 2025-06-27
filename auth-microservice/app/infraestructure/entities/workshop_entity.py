
from sqlalchemy import Column, DateTime, Integer, String, Boolean, func
from app.infraestructure.repository.conection_db import Base

class WorkShopEntity(Base):
    """
    Esta clase representa a la tabla workshop
    de la base de datos
    """
    __tablename__ = "workshop"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    activated = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())