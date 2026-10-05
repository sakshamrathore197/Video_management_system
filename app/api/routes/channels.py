from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.channel import Channel
from app.models.device import Device
from app.schemas.channel import ChannelCreate, ChannelResponse


router = APIRouter(
    prefix="/devices/{device_id}/channels",
    tags=["Channels"],
)


@router.post(
    "",
    response_model=ChannelResponse,
    status_code=201,
)
def create_channel(
    device_id: int,
    channel_data: ChannelCreate,
    db: Session = Depends(get_db),
):
    device = db.query(Device).filter(
        Device.id == device_id
    ).first()

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    channel = Channel(
        device_id=device_id,
        channel_number=channel_data.channel_number,
        name=channel_data.name,
        status=channel_data.status,
        enabled=channel_data.enabled,
    )

    db.add(channel)
    db.commit()
    db.refresh(channel)

    return channel


@router.get(
    "",
    response_model=list[ChannelResponse],
)
def get_channels(
    device_id: int,
    db: Session = Depends(get_db),
):
    device = db.query(Device).filter(
        Device.id == device_id
    ).first()

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return db.query(Channel).filter(
        Channel.device_id == device_id
    ).all()


@router.get(
    "/{channel_id}",
    response_model=ChannelResponse,
)
def get_channel(
    device_id: int,
    channel_id: int,
    db: Session = Depends(get_db),
):
    channel = db.query(Channel).filter(
        Channel.id == channel_id,
        Channel.device_id == device_id,
    ).first()

    if channel is None:
        raise HTTPException(
            status_code=404,
            detail="Channel not found",
        )

    return channel