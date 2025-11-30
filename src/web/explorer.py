from fastapi import APIRouter

router = APIRouter(prefix = "/explorer")


@router.get("/")
def first():
    return {"first explorer endpoint": 1}