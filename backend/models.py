from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nom: str
    longitude: float
    latitude: float
    grand: bool
    capture: bool
