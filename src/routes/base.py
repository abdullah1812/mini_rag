from fastapi import FastAPI, APIRouter, Depends
import os 
from helpers.config import get_settings,  Settings
base_router = APIRouter(
    prefix="/base/v1", # prefix خاص بالراوت دا 
    tags=['base_v1'], # اسم خاص بالراوت دا بس
)

@base_router.get("/")

async def welcom(app_setting : Settings =Depends(get_settings) ):
    # app_setting = get_setting()

    app_name = app_setting.APP_NAME
    app_ver = app_setting.APP_VERSION

    return {"message": f"welcom from {app_name} route"}
