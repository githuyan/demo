from fastapi import FastAPI

from common_libs import SetUp
from common_libs.common import constants
from demo.routes import api_router

app = FastAPI(title="demo系统", description="demo系统")


@app.on_event('startup')
async def startup_event():
    constants.SERVER_NAME = "default"
    app.include_router(api_router, prefix="/v1/api")
    await SetUp.setup_all("default")


# @app.on_event('shutdown')
# async def shutdown_event():
#     app.state.redis.close()
#     await app.state.redis.wait_closed()
