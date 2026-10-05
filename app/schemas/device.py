from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import DeviceStatus, DeviceType


class DeviceCreate(BaseModel):
    site_id: int
    name: str
    device_type: DeviceType
    manufacturer: str | None = None
    model: str | None = None
    ip_address: str | None = None
    status: DeviceStatus = DeviceStatus.UNKNOWN


class DeviceUpdate(BaseModel):
    name: str | None = None
    device_type: DeviceType | None = None
    manufacturer: str | None = None
    model: str | None = None
    ip_address: str | None = None
    status: DeviceStatus | None = None


class DeviceResponse(BaseModel):
    id: int
    site_id: int
    name: str
    device_type: DeviceType
    manufacturer: str | None
    model: str | None
    ip_address: str | None
    status: DeviceStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)