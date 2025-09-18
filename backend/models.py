from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Schtroumpf(Base):
    __tablename__ = "schtroumpfs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    grand = Column(Boolean, default=False)
    capture = Column(Boolean, default=False)
    description = Column(String)
