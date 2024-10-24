#pip install pywin32
import win32com.client

def printExcelFile(filePath, count):

    o = win32com.client.Dispatch('Excel.Application')
    o.visible = False
    wb = o.Workbooks.Open(filePath)
    ws = wb.Worksheets([1])
    ws.printout
    wb.Close(True)

