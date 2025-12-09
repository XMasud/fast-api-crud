from pydantic import BaseModel

# Shared properties
class ItemBase(BaseModel):
    title: str
    description: str
    is_active: bool = True

# Properties to receive on creation
class ItemCreate(ItemBase):
    pass

# Properties to return to client (includes ID)
class ItemResponse(ItemBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True # Important for ORM compatibility