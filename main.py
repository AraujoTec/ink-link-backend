
# from dateutil import tz
import uvicorn
import os
import sys

# Adicione o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
# app = FastAPI(docs_url="/docs", redoc_url="/doc")

from app.routers import healtcheck, usuarios


app = FastAPI()

app.include_router(healtcheck.router, prefix="/healcheck", tags=["Healtcheck"])
app.include_router(usuarios.router, prefix='/usuarios', tags=['Usuarios'])

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=8000, log_level="info"
    )  # , ssl_keyfile="key.pem", ssl_certfile="cert.pem")
