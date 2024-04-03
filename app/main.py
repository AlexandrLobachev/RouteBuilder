from fastapi import FastAPI

from app.tours.router import router as router_routes


app = FastAPI()

app.include_router(router_routes)
