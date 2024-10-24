import uvicorn
from fastapi import FastAPI
import json
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from models import ExcelPrintingRequest, ExcelPrintingResonse
from typing import List

from excel_print import printExcel,echoRequest,fileInfo
app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)



@app.get("/version")
async def version():
    return {"version":"1.0"}

@app.post("/print")
async def print(printRequest:ExcelPrintingRequest):    
    return printExcel(printRequest)

@app.post("/fileinfo")
async def fileinfo(printRequest:ExcelPrintingRequest):    
    return fileInfo(printRequest)

@app.post("/echo")
async def echo(printRequest:ExcelPrintingRequest):
    return echoRequest(printRequest)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)