from sqlalchemy.orm import Session
from . import models, schemas

def get_schtroumpfs(db: Session):
    return db.query(models.Schtroumpf).all()

def get_schtroumpf(db: Session, schtroumpf_id: int):
    return db.query(models.Schtroumpf).filter(models.Schtroumpf.id == schtroumpf_id).first()

def create_schtroumpf(db: Session, schtroumpf_in: schemas.SchtroumpfCreate):
    db_obj = models.Schtroumpf(**schtroumpf_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_capture(db: Session, schtroumpf_id: int):
    schtroumpf = get_schtroumpf(db, schtroumpf_id)
    if schtroumpf:
        schtroumpf.capture = True
        db.commit()
        db.refresh(schtroumpf)
    return schtroumpf