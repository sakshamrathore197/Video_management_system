from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.channel import Channel
from app.models.stream import Stream
from app.schemas.stream import StreamCreate, StreamResponse


router = APIRouter(
    prefix="/channels/{channel_id}/streams",
    tags=["Streams"],
)


@router.post(
    "",
    response_model=StreamResponse,
    status_code=201,
)
def create_stream(
    channel_id: int,
    stream_data: StreamCreate,
    db: Session = Depends(get_db),
):
    channel = db.query(Channel).filter(
        Channel.id == channel_id
    ).first()

    if channel is None:
        raise HTTPException(
            status_code=404,
            detail="Channel not found",
        )

    stream = Stream(
        channel_id=channel_id,
        name=stream_data.name,
        stream_type=stream_data.stream_type,
        protocol=stream_data.protocol,
        url=stream_data.url,
        codec=stream_data.codec,
        resolution=stream_data.resolution,
        fps=stream_data.fps,
        status=stream_data.status,
    )

    db.add(stream)
    db.commit()
    db.refresh(stream)

    return stream


@router.get(
    "",
    response_model=list[StreamResponse],
)
def get_streams(
    channel_id: int,
    db: Session = Depends(get_db),
):
    channel = db.query(Channel).filter(
        Channel.id == channel_id
    ).first()

    if channel is None:
        raise HTTPException(
            status_code=404,
            detail="Channel not found",
        )

    return db.query(Stream).filter(
        Stream.channel_id == channel_id
    ).all()


@router.get(
    "/{stream_id}",
    response_model=StreamResponse,
)
def get_stream(
    channel_id: int,
    stream_id: int,
    db: Session = Depends(get_db),
):
    stream = db.query(Stream).filter(
        Stream.id == stream_id,
        Stream.channel_id == channel_id,
    ).first()

    if stream is None:
        raise HTTPException(
            status_code=404,
            detail="Stream not found",
        )

    return stream