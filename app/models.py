from datetime import datetime, timezone

from sqlalchemy import Integer, Enum, Numeric, ForeignKey, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import enum


class Base(DeclarativeBase):
    pass


class StatusEnum(str, enum.Enum):
    running = "running"
    ended = "ended"


class Lot(Base):
    __tablename__ = "lot"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    starting_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), nullable=False)
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc)
    )


class Bid(Base):
    __tablename__ = "bid"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lot_id: Mapped[int] = mapped_column(ForeignKey("lot.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc)
    )
