from fastapi import FastAPI
from starlette.responses import RedirectResponse
from .routes.patentes import patente

app = FastAPI()

@app.get("/")
def home():
    return RedirectResponse(url="/docs/")

app.include_router(patente)