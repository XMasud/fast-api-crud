from pydantic import BaseModel
from datetime import datetime


# Shared properties
class ItemBase(BaseModel):
    title: str
    description: str
    is_active: bool = True

# Properties to receive on creation
class ItemCreate(ItemBase):
    pass

# Properties to return to client (includes ID)
class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool = True
    created_at: datetime

    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    }