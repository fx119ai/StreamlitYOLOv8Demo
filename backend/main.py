from ultralytics import YOLO
from typing import List
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    annotated_img: List[List[List[int]]]


# Instantiate FastAPI application
app = FastAPI()


@app.on_event("startup")
async def load_model():
    global model
    model = model = YOLO('models/yolov8n-pose.pt')


# Define a route for getting the server status
@app.get("/status")
async def get_status():
    return {"status": "Server is up and running!"}


# Define a route for getting a prediction
@app.post("/get_prediction", response_model=PredictionResponse)
async def get_prediction(file: UploadFile = File(...)):
    orig_img = Image.open(io.BytesIO(await file.read()))
    pred = model(orig_img)
    annotated_img = pred[0].plot().tolist()
    return PredictionResponse(annotated_img=annotated_img)