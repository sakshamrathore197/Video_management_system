from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SiteCreate(BaseModel):
    name: str
    description: str | None = None
    location: str | None = None
    status: str = "active"

class SiteUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    location: str | None = None
    status: str | None = None

class SiteResponse(BaseModel):
    id: int
    name: str
    description: str | None
    location: str | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)