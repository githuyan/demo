from fastapi import APIRouter

from demo.handlers import generator


router = APIRouter()

router.add_api_route(
    path='.snow_flake.get',
    endpoint=generator.get_snow_flake_id,
    methods=['get'],
    summary='雪花算法ID生成器',
    # response_model=SuccessBaseModel
)
