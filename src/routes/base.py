from fastapi import FastAPI, APIRouter


base_route = APIRouter(
    # prefix="/base/v1", # prefix خاص بالراوت دا 
    tags=['base_v1'] # اسم خاص بالراوت دا بس
)

@base_route.get("/")
def base_r():
    return {"message": "welcom from base route"}
