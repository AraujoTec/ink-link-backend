from fastapi import APIRouter, Depends
from datetime import datetime

router = APIRouter()

@router.get('/')
async def healtcheck():
    return str(datetime.now())