from pydantic import BaseModel


class ExcelPrintingRequest(BaseModel):
    content: str | None = None
    count: int| None = 0
    title: str| None = None

class ExcelPrintingResonse(BaseModel):
    resultCode: int | None = None
    message: str | None = None
    fileLength: int | None = None
    originalLength: int | None = None
    fileName: str | None = None