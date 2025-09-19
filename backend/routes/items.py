from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, database, schemas

router = APIRouter(prefix="/items", tags=["items"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Schtroumpf])
def list_items(db: Session = Depends(get_db)):
    return crud.get_schtroumpfs(db)

@router.post("/", response_model=schemas.Schtroumpf)
def create_item(schtroumpf_in: schemas.SchtroumpfCreate, db: Session = Depends(get_db)):
    return crud.create_schtroumpf(db, schtroumpf_in)

@router.put("/{item_id}/capture", response_model=schemas.Schtroumpf)
def capture_item(item_id: int, db: Session = Depends(get_db)):
    updated = crud.update_capture(db, item_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Schtroumpf non trouvé")
    return updated