
# from dateutil import tz
import uvicorn
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
# app = FastAPI(docs_url="/docs", redoc_url="/doc")

from app.routers import healtcheck


app = FastAPI()

app.include_router(healtcheck.router, prefix="/healcheck", tags=["Healtcheck"])
