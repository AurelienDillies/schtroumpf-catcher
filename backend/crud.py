import json
from pathlib import Path
from typing import List, Optional
from .models import Item

DB_FILE = Path(__file__).parent / "schtroumpfs.json"

def read_db() -> List[dict]:
    if not DB_FILE.exists():
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_db(data: List[dict]):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_items() -> List[Item]:
    return [Item(**item) for item in read_db()]

def get_item(item_id: int) -> Optional[Item]:
    for item in read_db():
        if item["id"] == item_id:
            return Item(**item)
    return None

def create_item(item: Item) -> Item:
    data = read_db()
    if any(existing["id"] == item.id for existing in data):
        raise ValueError("Un item avec cet ID existe déjà")
    data.append(item.dict())
    write_db(data)
    return item

def update_item(item_id: int, new_item: Item) -> Optional[Item]:
    data = read_db()
    for i, existing in enumerate(data):
        if existing["id"] == item_id:
            data[i] = new_item.dict()
            write_db(data)
            return new_item
    return None

def delete_item(item_id: int) -> bool:
    data = read_db()
    new_data = [item for item in data if item["id"] != item_id]
    if len(new_data) == len(data):
        return False
    write_db(new_data)
    return True
