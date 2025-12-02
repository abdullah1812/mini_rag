from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="/base/v1", # prefix خاص بالراوت دا 
    tags=['base_v1'], # اسم خاص بالراوت دا بس
)

@base_router.get("/")
async def welcom():
    return {"message": "welcom from base route"}
