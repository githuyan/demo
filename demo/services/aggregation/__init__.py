from fastapi import APIRouter


from . import generator


api_router = APIRouter()

api_router.include_router(generator.router, prefix="/generator", tags=["generator.tag"])