from fastapi import APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings,  Settings
from controllers.DataController import DataController
from controllers.ProjectController import ProjectController
import os ,  aiofiles
from models import ResponseEnums
import logging

logger =  logging.getLogger('uvicorn.eror')
data_rout = APIRouter(prefix="/data") 

@data_rout.post("/upload/{project_id}")
async def uploadfiles(project_id:str, file: UploadFile, app_setting: Settings = Depends(get_settings)):
    
    # app_setting: Settings = Depends(get_settings)
    # validate the file
    is_valid, signal = DataController().validate_uploaded_file(file=file)
    
    if not is_valid: 
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":signal
            }
        )
    new_file_name = str(project_id)+ '_'+ str(file.filename)
    project_dir_path = ProjectController().get_project_path(project_id)
    file_path = os.path.join(project_dir_path, new_file_name)
    
    try: 
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_setting.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":ResponseEnums.FILE_UPLOADED_FAILD.value
            }
        )

     
    return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={
                "signal":ResponseEnums.FILE_UPLOADED_SUCCES.value
            }
        )

