# backend/schemas.py
from pydantic import BaseModel

class SchtroumpfBase(BaseModel):
    nom: str
    longitude: float
    latitude: float
    grand: bool = False
    capture: bool = False
    description: str = ""

class SchtroumpfCreate(SchtroumpfBase):
    pass

class Schtroumpf(SchtroumpfBase):
    id: int
    class Config:
        orm_mode = True
