from fastapi import FastAPI, APIRouter, status
from fastapi.responses import JSONResponse
from app.server.api.v1.climate import router as climate_router


app = FastAPI()

app.include_router(climate_router)


@app.get("/api/v1/welcome")
def welcome(name: str = "Climate Buddy Bot"):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"Welcome to, {name}!"})

@app.get("/")
def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Welcome to Climate Buddy Bot!"})
