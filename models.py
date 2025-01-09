import enum

from sqlalchemy import String, JSON, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.inspection import inspect
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
    strategies = relationship("TradingStrategy", back_populates="owner")

    def to_json(self) -> dict[str, int | str]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }

    def __repr__(self) -> str:
        return f"User: {self.first_name} {self.last_name}"


class TradingStrategy(db.Model):
    __tablename__ = "trading_strategies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    asset_type: Mapped[str] = mapped_column(String(30), nullable=False)
    buy_condition: Mapped[JSON] = mapped_column(JSON, nullable=False)
    sell_condition: Mapped[JSON] = mapped_column(JSON, nullable=False)
    status: Mapped[TradingStatus] = mapped_column(Enum(TradingStatus), nullable=False, default=TradingStatus.active)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped[User] = relationship(back_populates="strategies")

    def to_json(self) -> dict:
        return {column.key: getattr(self, column.key) for column in inspect(self).mapper.columns}

    def __repr__(self) -> str:
        return f"Trading Strategy: {self.name}"
