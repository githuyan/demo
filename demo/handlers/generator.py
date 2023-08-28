from fastapi import Query

from common_libs.common.snow_flake import SnowflakeIDGenerator


async def get_snow_flake_id(amount: int = Query(default=1, min=1, description="生成ID数量")):

    generator = SnowflakeIDGenerator(machine_id=1)
    ids = [generator.generate_id() for _ in range(amount)]

    return ids
