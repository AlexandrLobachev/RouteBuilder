from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select

from app.tours.models import Point, Route
from app.database import async_session_maker


class PointDAO():

    @classmethod
    async def add_points(cls, values):
        async with async_session_maker() as session:
            stmt = insert(Point).values(values)
            stmt = stmt.on_conflict_do_nothing()
            await session.execute(stmt)
            await session.commit()
            return


class RouteDAO():

    @classmethod
    async def create_route(cls, route):
        async with async_session_maker() as session:
            new_route = insert(Route).values(route=route).returning(Route)
            result = await session.execute(new_route)
            await session.commit()
            return result.scalar_one()

    @classmethod
    async def get_route(cls, id):
        async with async_session_maker() as session:
            query = select(Route).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
