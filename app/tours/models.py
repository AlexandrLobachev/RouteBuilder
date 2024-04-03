from typing import Optional
from sqlalchemy import UniqueConstraint, ARRAY, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Point(Base):
    __tablename__='points'

    id: Mapped[int] = mapped_column(primary_key=True)
    zip: Mapped[Optional[int]]
    lat: Mapped[float]
    lng: Mapped[float]
    city: Mapped[Optional[str]]
    state_id: Mapped[Optional[str]]
    state_name: Mapped[Optional[str]]
    zcta: Mapped[Optional[str]]
    parent_zcta: Mapped[Optional[str]]
    population: Mapped[Optional[str]]
    density: Mapped[Optional[str]]
    county_fips: Mapped[Optional[str]]
    county_name: Mapped[Optional[str]]
    county_weights: Mapped[Optional[str]]
    county_names_all: Mapped[Optional[str]]
    county_fips_all: Mapped[Optional[str]]
    imprecise: Mapped[Optional[str]]
    military: Mapped[Optional[str]]
    timezone: Mapped[Optional[str]]

    __table_args__ =(
        UniqueConstraint("lat", "lng", name="coordinates"),
    )


class Route(Base):
    __tablename__='routes'

    id: Mapped[int] = mapped_column(primary_key=True)
    route: Mapped[Optional[list[float]]] = mapped_column(ARRAY(Float))
