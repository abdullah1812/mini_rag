from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseEnums
class DataController(BaseController):
    def __init__(self):
        super().__init__()

        self.size_scale = 1048576 


    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in  self.app_settings.FILE_AVAILABLE_TYPES:
            return False, ResponseEnums.FILE_TYPE_NOT_SUPPORTED.value
        

            # Read file in sync mode
        content = file.file.read()
        file_size = len(content)
        file.file.seek(0)  # Reset pointer so FastAPI can read again

        # Validate size
        if file_size > self.size_scale * self.app_settings.FILE_MAX_SIZE:
            return False, ResponseEnums.FILE_SIZE_EXCEEDED.value
            # ResponseSignel.FILE_TYPE_NOT_SUPORTED.value

        return True, ResponseEnums.FILE_VALIDATED_SUCCES.value
