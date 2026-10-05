from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChannelCreate(BaseModel):
    channel_number: int
    name: str
    status: str = "UNKNOWN"
    enabled: bool = True


class ChannelUpdate(BaseModel):
    channel_number: int | None = None
    name: str | None = None
    status: str | None = None
    enabled: bool | None = None


class ChannelResponse(BaseModel):
    id: int
    device_id: int
    channel_number: int
    name: str
    status: str
    enabled: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)