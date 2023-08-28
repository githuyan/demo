from fastapi import FastAPI

from demo.routes import api_router

app = FastAPI(title="demo系统", description="demo系统")


@app.on_event('startup')
async def startup_event():
    # constants.SERVER_NAME = "default"
    app.include_router(api_router, prefix="/v1/api")


@app.on_event('shutdown')
async def shutdown_event():
    await app.state.close()
