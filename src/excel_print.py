
import base64
import tempfile


from models import ExcelPrintingRequest, ExcelPrintingResonse
from excel_print_windows import printExcelFile





def echoRequest(request: ExcelPrintingRequest):
    return request

def mustBeLessThan3(count):
    resp=ExcelPrintingResonse()
    resp.resultCode=1
    resp.message="count must be less than 3, get: "+str(count)
    return resp

def paramIsMust(paramName):
    resp=ExcelPrintingResonse()
    resp.resultCode=1
    resp.message=paramName+" must be specified"
    return resp

def printExcel(request: ExcelPrintingRequest):
    if request.count == None:
        return paramIsMust("count")
    if request.title == None:
        return paramIsMust("title")
    if request.content == None:
        return paramIsMust("content")
    if request.count >= 3:
        return mustBeLessThan3(request.count)
    return printExcelFile(request)


def fileInfo(request: ExcelPrintingRequest):

    if request.count == None:
        return paramIsMust("count")
    if request.title == None:
        return paramIsMust("title")
    if request.content == None:
        return paramIsMust("content")
    if request.count >= 3:
        return mustBeLessThan3(request.count)


    tmp = tempfile.NamedTemporaryFile()
   
    resp=ExcelPrintingResonse()
    resp.resultCode=0
    resp.message="success"
    content=base64.b64decode(request.content)
    with open(tmp.name, 'w+b') as f:
        f.write(content) # where `stuff` is, y'know... stuff to write (a string)
    resp.fileLength = len(content)
    resp.originalLength=len(request.content)
    resp.fileName = tmp.name
    return resp

