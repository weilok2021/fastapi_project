from fastapi import FastAPI
from pydantic import BaseModel
from web import explorer

app = FastAPI()
app.include_router(explorer.router)

@app.get("/")
def index() -> tuple[str,str,str]:
    return ("name", "salary", "area")


