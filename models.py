import enum

from sqlalchemy import String, JSON, Enum
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TradingStatus(enum.Enum):
    active = "active"
    inactive = "inactive"


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    def __repr__(self) -> str:
        return f"User: {self.first_name} {self.last_name}"


class TradingStrategy(db.Model):
    __tablename__ = "trading_strategy"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    asset_type: Mapped[str] = mapped_column(String(30), nullable=False)
    buy_condition: Mapped[JSON] = mapped_column(JSON, nullable=False)
    sell_condition: Mapped[JSON] = mapped_column(JSON, nullable=False)
    status: Mapped[TradingStatus] = mapped_column(Enum(TradingStatus), nullable=False, default=TradingStatus.active)

    def __repr__(self) -> str:
        return f"Trading Strategy: {self.name}"
