from fastapi import APIRouter, UploadFile, Depends
from helpers.config import Settings, get_setting
from controllers import DataController
data_rout = APIRouter(prefix="/data")

@data_rout.post("/upload/{project_id}")
async def uploadfiles(project_id:str, file: UploadFile, app_setting: Settings = Depends(get_setting)):
    

    # validate the file

    is_valid, signal =  DataController().vlaidate_uploaded_file(file = file)

    return {
        "signal": signal
    }