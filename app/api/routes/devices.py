from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.device import Device
from app.models.site import Site
from app.schemas.device import DeviceCreate, DeviceResponse


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.post(
    "",
    response_model=DeviceResponse,
    status_code=201,
)
def create_device(
    device_data: DeviceCreate,
    db: Session = Depends(get_db),
):
    site = db.query(Site).filter(
        Site.id == device_data.site_id
    ).first()

    if site is None:
        raise HTTPException(
            status_code=404,
            detail="Site not found",
        )

    device = Device(
        site_id=device_data.site_id,
        name=device_data.name,
        device_type=device_data.device_type,
        manufacturer=device_data.manufacturer,
        model=device_data.model,
        ip_address=device_data.ip_address,
        status=device_data.status,
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


@router.get(
    "",
    response_model=list[DeviceResponse],
)
def get_devices(
    db: Session = Depends(get_db),
):
    return db.query(Device).all()


@router.get(
    "/{device_id}",
    response_model=DeviceResponse,
)
def get_device(
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

    return device