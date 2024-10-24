#pip install pywin32
import win32com.client
from models import ExcelPrintingRequest, ExcelPrintingResonse
import tempfile
import base64

def printExcelFileInternal(fileName):
    
    o = win32com.client.Dispatch('Excel.Application')
    o.visible = False
    wb = o.Workbooks.Open(fileName)
    ws = wb.Worksheets([1])
    ws.printout
    wb.Close(True)

    return 1
    

def printExcelFile(request:ExcelPrintingRequest):

    

    tmp = tempfile.NamedTemporaryFile()
   
    resp=ExcelPrintingResonse()
    resp.resultCode=0
    resp.message="success with simulate mode"
    content=base64.b64decode(request.content)
    with open(tmp.name, 'w+b') as f:
        f.write(content) # where `stuff` is, y'know... stuff to write (a string)

    printExcelFileInternal(tmp.name)

    resp.fileLength = len(content)
    resp.originalLength=len(request.content)
    resp.fileName = tmp.name

    return resp