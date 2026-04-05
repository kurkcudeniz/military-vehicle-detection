from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = FastAPI(
    title="Military Vehicle Detection API",
    description="Detect and classify military vehicles: Aircraft, AFV, APC, LAV, MEV",
    version="1.0.0"
)

model = YOLO("models/best.pt")

CLASS_INFO = {
    "Aircraft": "Military aircraft",
    "Armoured Fighting Vehicle-AFV-": "Tank or armoured combat vehicle",
    "Armoured Personal Carrier-APC-": "Troop transport vehicle",
    "Light Armoured Vehicle-LAV-": "Light reconnaissance vehicle",
    "Military engineering vehicle-MEV-": "Engineering/support vehicle"
}

@app.get("/")
def root():
    return {
        "service": "Military Vehicle Detection API",
        "version": "1.0.0",
        "classes": list(CLASS_INFO.keys()),
        "status": "active"
    }

@app.post("/detect")
async def detect(file: UploadFile = File(...), conf: float = 0.3):
    contents = await file.read()
    arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    
    results = model(img, conf=conf)
    
    detections = []
    for box in results[0].boxes:
        cls_name = model.names[int(box.cls)]
        confidence = round(float(box.conf) * 100, 1)
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        detections.append({
            "class": cls_name,
            "description": CLASS_INFO.get(cls_name, "Unknown"),
            "confidence": confidence,
            "bbox": {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        })
    
    return {
        "total_detections": len(detections),
        "detections": detections
    }

@app.post("/detect/visual")
async def detect_visual(file: UploadFile = File(...), conf: float = 0.3):
    contents = await file.read()
    arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    
    results = model(img, conf=conf)
    annotated = results[0].plot()
    
    os.makedirs("results", exist_ok=True)
    cv2.imwrite("results/latest.jpg", annotated)
    return FileResponse("results/latest.jpg", media_type="image/jpeg")
