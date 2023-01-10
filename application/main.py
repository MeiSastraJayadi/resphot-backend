from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException 
from fastapi.requests import Request
from fastapi.responses import FileResponse, JSONResponse, Response
from .image_processor.main_proc import function_to_restore
from .image_processor.colorization import coloring_image
import tensorflow as tf
import numpy as np
import uuid


app = FastAPI()
IMAGE_DIR = "./application/images/"


@app.get("/")
def show_hello() : 
    return JSONResponse({"data" : "Hello World"}, status_code=200)

@app.post("/upload-image")
async def upload_image(file : UploadFile) : 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    with open(f"{IMAGE_DIR}{file.filename}", "wb") as f : 
        f.write(contents)
    img = function_to_restore(f"{IMAGE_DIR}{file.filename}")    
    return FileResponse(f"{IMAGE_DIR}{file.filename}")

@app.post("/coloring")
async def coloring(file : UploadFile) : 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    with open(f"{IMAGE_DIR}{file.filename}", "wb") as f : 
        f.write(contents)
    coloring_image(f"{IMAGE_DIR}{file.filename}")    
    return FileResponse(f"{IMAGE_DIR}{file.filename}")
    return 



