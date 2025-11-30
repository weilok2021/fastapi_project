from fastapi import FastAPI
from pydantic import BaseModel
from web import explorer, creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)


