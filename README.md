# Military Vehicle Detection and Classification System

An AI-powered military vehicle detection system using YOLOv8, trained on satellite and aerial imagery to identify and classify 5 types of military vehicles.

## Detection Classes

| Class | Description | mAP50 |
|-------|------------|-------|
| Aircraft | Military aircraft | 78.0% |
| AFV (Armoured Fighting Vehicle) | Tanks, armoured combat vehicles | 71.3% |
| APC (Armoured Personal Carrier) | Troop transport vehicles | 80.0% |
| LAV (Light Armoured Vehicle) | Light reconnaissance vehicles | 87.9% |
| MEV (Military Engineering Vehicle) | Engineering/support vehicles | 90.3% |

**Overall Performance: 81.5% mAP50**

## Sample Results

<p align="center">
  <img src="results/tank.jpg" width="400"/>
  <img src="results/helicopter.jpg" width="400"/>
</p>
<p align="center">
  <img src="results/apc.jpg" width="400"/>
</p>

## Tech Stack

- **Model:** YOLOv8 (Ultralytics)
- **Training:** Google Colab + Tesla T4 GPU
- **Dataset:** 2,794 annotated military vehicle images (Roboflow)
- **API:** FastAPI + Uvicorn
- **Language:** Python 3.10+

## Quick Start

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/military-vehicle-detection.git
cd military-vehicle-detection
pip install -r requirements.txt
```

### Run Detection on Image
```bash
python src/detect.py path/to/image.jpg
```

### Run API Server
```bash
cd military-vehicle-detection
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

Then open http://localhost:8000/docs for Swagger UI.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info and available classes |
| POST | `/detect` | Returns JSON with detections |
| POST | `/detect/visual` | Returns annotated image |

### Example API Request
```bash
curl -X POST "http://localhost:8000/detect" \
  -F "file=@test_image.jpg" \
  -F "conf=0.3"
```

### Example Response
```json
{
  "total_detections": 2,
  "detections": [
    {
      "class": "Armoured Fighting Vehicle-AFV-",
      "description": "Tank or armoured combat vehicle",
      "confidence": 83.0,
      "bbox": {"x1": 45, "y1": 30, "x2": 890, "y2": 620}
    }
  ]
}
```

## Training Details

- **Base Model:** YOLOv8n (pretrained on COCO)
- **Transfer Learning:** Fine-tuned on military vehicle dataset
- **Epochs:** 50
- **Image Size:** 640x640
- **Batch Size:** 16
- **Training Time:** ~18 minutes on Tesla T4

## Project Structure
## Future Improvements

- [ ] Add satellite imagery support (xView dataset)
- [ ] Real-time video stream processing
- [ ] Docker containerization
- [ ] Web dashboard with detection analytics
- [ ] Multi-object tracking (ByteTrack)
- [ ] Model optimization for edge deployment (TensorRT)

## Author

**Deniz Kurkcu** — Software Engineer | Computer Vision & Defense Technology

## License

MIT License
