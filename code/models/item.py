from db import data
from typing import Optional
from pydantic import BaseModel


class ItemModel(BaseModel):
    __tablename__ = 'items'
    
    reel: int
    date: str
    site_nom: str
    prevision: Optional[int]
    site_type: str
    
    @classmethod
    def find_by_name(cls, name):
        name = name.upper()
        return next((cls(**item).dict() for item in data if item["site_nom"] == name), None)

    @classmethod
    def find_all(cls):
        return data