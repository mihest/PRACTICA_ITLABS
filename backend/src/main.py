from contextlib import asynccontextmanager

import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.admins.main import init_admin
from . import api_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_admin(app)
    yield

app = FastAPI(
    title="Backend",
    docs_url='/ui-swagger',
    openapi_url="/openapi.json",
    lifespan=lifespan
)

app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(
    api_routers,
    prefix='/api',
)




app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods='*',
    allow_headers='*',
)


if __name__ == '__main__':
    uvicorn.run("src.main:app", host='0.0.0.0', port=8081, log_level='info', reload=True)