from fastapi import FastAPI
from pydantic import BaseModel
from web import explorer

app = FastAPI()
app.include_router(explorer.router)


