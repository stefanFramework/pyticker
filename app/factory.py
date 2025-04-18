from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.middlewares.auth import AuthMiddleware
from app.api.routes import utils


def create_app():
    app = FastAPI()
    create_api(app)
    return app


def create_api(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(AuthMiddleware)

    app.include_router(utils.router, prefix="/utils")



