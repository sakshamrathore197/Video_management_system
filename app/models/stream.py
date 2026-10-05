from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Stream(Base):
    __tablename__ = "streams"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    stream_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    protocol: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    codec: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    resolution: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    fps: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="unknown",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    channel = relationship(
        "Channel",
        back_populates="streams",
    )