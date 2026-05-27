import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from app.api.routes import router
from app.core.config import settings
from app.core.logger import logger

api = FastAPI(
    title=settings.APP_NAME,
    description="Agentic AI powered bug analysis API"
)


def configure_routes():
    api.include_router(router, prefix="/api", tags=["Analysis"])


def configure_static():
    api.mount(
        "/static",
        StaticFiles(directory="app/static"),
        name="static"
    )


def create_app():
    configure_routes()
    configure_static()
    logger.info("Analysis app started.")
    return api


# initialize app
create_app()

@router.get("/health")
def health():
    response = {
        "status":"healthy"
    }
    logger.info(f"App health { response }")
    return JSONResponse(content=response, status_code=200)


@api.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global error occured. Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal server error"
        }
    )


# local execution
if __name__ == "__main__":
    uvicorn.run(
        "app.main:api",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG
    )