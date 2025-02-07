from fastapi import FastAPI
from app.routers import workstation
#from db import database
app=FastAPI()
app.include_router(workstation.router)
@app.get("/")
def base_api():
    return{"welcome the workstation FastAPI"}
