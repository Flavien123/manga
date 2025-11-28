from fastapi import FastAPI
from uvicorn import run

from presentation.api import router as api_router

app = FastAPI()

app.include_router(router=api_router)

if __name__ == "__main__":
    run("main:app", reload=True)