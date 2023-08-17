from fastapi import Query

from common_libs.clutter_utils.snow_flake import SnowflakeIDGenerator
from common_libs.cache_utils.cache import get_redis_connection


async def get_snow_flake_id(amount: int = Query(default=1, min=1, description="生成ID数量")):
    generator = SnowflakeIDGenerator(machine_id=1)
    ids = [generator.generate_id() for _ in range(amount)]
    
    conn = await get_redis_connection()
    data = await conn.get("aa")
    print(f"-------{data}------")
    return ids
