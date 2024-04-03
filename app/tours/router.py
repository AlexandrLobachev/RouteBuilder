from fastapi import APIRouter, HTTPException
from fastapi import File, UploadFile
from app.tours.dao import PointDAO, RouteDAO
from app.tours.loader import get_data_from_csv
from app.tours.route_builder import get_tour_coord

router = APIRouter(
    prefix='/api/routes',
    tags=['Маршруты'],
)


@router.get('/{id}')
async def get_route(id: int):
    result = await RouteDAO.get_route(id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Маршрут не существует.")
    return {
        'id': result.id,
        'points': [{'lat': coord[0], 'lng': coord[1]} for coord in result.route]
    }

@router.post("/")
async def upload(format: str, file: UploadFile = File(...)):
    if format != 'csv':
        return {
            'message': 'Поддерживаеться только CSV.'
        }
    data = get_data_from_csv(file)
    await PointDAO.add_points(values=data)
    opt_route = get_tour_coord(data)
    result = await  RouteDAO.create_route(route=opt_route)
    return {
        'id': result.id,
        'points': [{'lat': coord[0], 'lng': coord[1]} for coord in result.route]
    }
