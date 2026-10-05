from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import StreamProtocol, StreamType


class StreamCreate(BaseModel):
    name: str
    stream_type: StreamType
    protocol: StreamProtocol
    url: str
    codec: str | None = None
    resolution: str | None = None
    fps: int | None = None
    status: str = "UNKNOWN"


class StreamUpdate(BaseModel):
    name: str | None = None
    stream_type: StreamType | None = None
    protocol: StreamProtocol | None = None
    url: str | None = None
    codec: str | None = None
    resolution: str | None = None
    fps: int | None = None
    status: str | None = None


class StreamResponse(BaseModel):
    id: int
    channel_id: int
    name: str
    stream_type: StreamType
    protocol: StreamProtocol
    url: str
    codec: str | None
    resolution: str | None
    fps: int | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)