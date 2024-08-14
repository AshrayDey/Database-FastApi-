from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes=True  # Updated from 'orm_mode' to 'from_attributes' if applicable

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: Optional[List[Item]] = []  # Use List from typing

    class Config:
        from_attributes=True   # Updated from 'orm_mode' to 'from_attributes' if applicable
