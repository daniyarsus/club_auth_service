import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.api.controllers import setup_controllers


def build_app() -> FastAPI:
    app = FastAPI(
        title="Club AUTH service Swagger UI",
        description="Naruto > OnePiece",
        version="1.0.0",
        contact={
            "name": "Daniyar senior dev 69 years of developing :D",
            "url": "https://github.com/daniyarsus/"
        }
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    setup_controllers(app.router)

    return app


if __name__ == "__main__":
    uvicorn.run(
        app="src.presentation.main:build_app",
        factory=True,
        host="0.0.0.0",
        port=8000,
        workers=1
    )
