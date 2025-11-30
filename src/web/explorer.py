from fastapi import APIRouter
from fake import explorer as service

router = APIRouter(prefix = "/explorer")


@router.get("/")
def first():
    return {"first explorer endpoint": 1}