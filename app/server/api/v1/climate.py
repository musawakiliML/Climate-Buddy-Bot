from fastapi import FastAPI, APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/api/v1/climate")
def climate():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message":"Climate Buddy Bot"})
