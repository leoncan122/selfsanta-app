from  fastapi import FastAPI
from loguru import logger
from uuid import uuid4
from fastapi.responses import JSONResponse
from app.gateway.api_router import call_api_gateway
from app.controllers.system import router

from app.users_mgt import users_main

from app.celery.funds import celery


app = FastAPI()
from starlette.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, dependencies=[call_api_gateway],prefix="/system")

@app.middleware("http")
async def log_middleware(request: str, call_next): 
    
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info(f"Request: {request.url.path}")
        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(f"Error: {e}")
            response = JSONResponse(status_code=500, content={"message": "Internal server error"})
        finally:
            logger.info("Middleware finished" + request.url.path)
            return response
        
app.mount("/api", users_main.app)


if __name__ == "__main__":
    celery.worker_main("worker", "--loglevel=INFO")