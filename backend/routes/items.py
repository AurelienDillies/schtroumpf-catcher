from fastapi import APIRouter, HTTPException
from .. import crud, models

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=list[models.Item])
def list_items():
    return crud.get_items()

@router.get("/{item_id}", response_model=models.Item)
def read_item(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return item

@router.post("/", response_model=models.Item)
def create_item(item: models.Item):
    try:
        return crud.create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{item_id}", response_model=models.Item)
def update_item(item_id: int, new_item: models.Item):
    updated = crud.update_item(item_id, new_item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return updated

@router.delete("/{item_id}")
def delete_item(item_id: int):
    deleted = crud.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return {"message": "Item supprimé avec succès"}
