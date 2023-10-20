from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.types import String


class Base(DeclarativeBase):
    pass


class School(Base):
    __tablename__ = 'schools'
    school_id: Mapped[str] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(15))
    country: Mapped[str] = mapped_column(String(50))
