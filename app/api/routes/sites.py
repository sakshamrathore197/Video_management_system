from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.site import Site
from app.schemas.site import SiteCreate, SiteResponse, SiteUpdate


router = APIRouter(
    prefix="/sites",
    tags=["Sites"],
)


@router.post(
    "",
    response_model=SiteResponse,
    status_code=201,
)
def create_site(
    site_data: SiteCreate,
    db: Session = Depends(get_db),
):
    site = Site(
        name=site_data.name,
        description=site_data.description,
        location=site_data.location,
        status=site_data.status,
    )

    db.add(site)
    db.commit()
    db.refresh(site)

    return site


@router.get(
    "",
    response_model=list[SiteResponse],
)
def get_sites(
    db: Session = Depends(get_db),
):
    return db.query(Site).all()


@router.get(
    "/{site_id}",
    response_model=SiteResponse,
)
def get_site(
    site_id: int,
    db: Session = Depends(get_db),
):
    site = db.query(Site).filter(
        Site.id == site_id
    ).first()

    if site is None:
        raise HTTPException(
            status_code=404,
            detail="Site not found",
        )

    return site