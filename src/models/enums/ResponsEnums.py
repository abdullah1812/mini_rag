from enum import Enum

class ResponseEnums(Enum):
    FILE_VALIDATED_SUCCES = "File Validated Succes"
    FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXCEEDED = "File Size Exceeded"
    FILE_UPLOADED_SUCCES = "File Uploaded Succes"
    FILE_UPLOADED_FAILD = "File Uploaded Falid"