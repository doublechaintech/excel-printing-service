#pip install pywin32

from models import ExcelPrintingRequest, ExcelPrintingResonse
import tempfile
import base64


def printExcelFile(request:ExcelPrintingRequest):

    

    tmp = tempfile.NamedTemporaryFile()
   
    resp=ExcelPrintingResonse()
    resp.resultCode=0
    resp.message="success with simulate mode"
    content=base64.b64decode(request.content)
    with open(tmp.name, 'w+b') as f:
        f.write(content) # where `stuff` is, y'know... stuff to write (a string)
    resp.fileLength = len(content)
    resp.originalLength=len(request.content)
    resp.fileName = tmp.name

    return resp



