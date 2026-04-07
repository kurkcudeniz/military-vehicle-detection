# Military Vehicle Detection and Classification System

AI-powered military vehicle detection and classification system using YOLOv8, trained on aerial and satellite imagery to identify 5 types of military vehicles.

## Demo

<p align="center">
  <img src="results/tank.jpg" width="400"/>
  <img src="results/helicopter.jpg" width="400"/>
</p>
<p align="center">
  <img src="results/apc.jpg" width="400"/>
</p>

## Performance

| Class | Description | mAP50 |
|-------|------------|-------|
| Aircraft | Military aircraft/helicopters | 78.0% |
| AFV (Armoured Fighting Vehicle) | Tanks, armoured combat vehicles | 71.3% |
| APC (Armoured Personal Carrier) | Troop transport vehicles | 80.0% |
| LAV (Light Armoured Vehicle) | Light reconnaissance vehicles | 87.9% |
| MEV (Military Engineering Vehicle) | Engineering/support vehicles | 90.3% |
| **Overall** | **All classes** | **81.5%** |

## Features

- **Real-time Detection** — YOLOv8 model with ONNX optimization (21ms inference)
- **REST API** — FastAPI service with Swagger documentation
- **Web Dashboard** — Streamlit-based interactive UI
- **Video Processing** — Frame-by-frame detection on video files
- **Object Tracking** — ByteTrack multi-object tracking
- **Docker Support** — One-command deployment

## Tech Stack

- **Model:** YOLOv8n + ONNX Runtime
- **Training:** Google Colab, Tesla T4 GPU, 50 epochs
- **Dataset:** 2,794 annotated military vehicle images (Roboflow)
- **API:** FastAPI + Uvicorn
- **Frontend:** Streamlit
- **Deployment:** Docker
- **Language:** Python 3.11

## Quick Start

### Option 1: Docker (Recommended)

```bash
cd ~/military-vehicle-detection
cat << 'READMEEOF' > README.md
# Military Vehicle Detection and Classification System

AI-powered military vehicle detection and classification system using YOLOv8, trained on aerial and satellite imagery to identify 5 types of military vehicles.

## Demo

<p align="center">
  <img src="results/tank.jpg" width="400"/>
  <img src="results/helicopter.jpg" width="400"/>
</p>
<p align="center">
  <img src="results/apc.jpg" width="400"/>
</p>

## Performance

| Class | Description | mAP50 |
|-------|------------|-------|
| Aircraft | Military aircraft/helicopters | 78.0% |
| AFV (Armoured Fighting Vehicle) | Tanks, armoured combat vehicles | 71.3% |
| APC (Armoured Personal Carrier) | Troop transport vehicles | 80.0% |
| LAV (Light Armoured Vehicle) | Light reconnaissance vehicles | 87.9% |
| MEV (Military Engineering Vehicle) | Engineering/support vehicles | 90.3% |
| **Overall** | **All classes** | **81.5%** |

## Features

- **Real-time Detection** — YOLOv8 model with ONNX optimization (21ms inference)
- **REST API** — FastAPI service with Swagger documentation
- **Web Dashboard** — Streamlit-based interactive UI
- **Video Processing** — Frame-by-frame detection on video files
- **Object Tracking** — ByteTrack multi-object tracking
- **Docker Support** — One-command deployment

## Tech Stack

- **Model:** YOLOv8n + ONNX Runtime
- **Training:** Google Colab, Tesla T4 GPU, 50 epochs
- **Dataset:** 2,794 annotated military vehicle images (Roboflow)
- **API:** FastAPI + Uvicorn
- **Frontend:** Streamlit
- **Deployment:** Docker
- **Language:** Python 3.11

## Quick Start

### Option 1: Docker (Recommended)

```bash
docker build -t military-vehicle-detection .
docker run -p 8000:8000 military-vehicle-detection
```

Then open http://localhost:8000/docs

### Option 2: Local Installation

```bash
git clone https://github.com/kurkcudeniz/military-vehicle-detection.git
cd military-vehicle-detection
pip install -r requirements.txt
```

### Run Detection

```bash
python src/detect.py path/to/image.jpg --conf 0.3
```

### Run API

```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

### Run Dashboard

```bash
streamlit run src/app.py
```

### Run Video Detection

```bash
python src/video_detect.py path/to/video.mp4
```

### Run Live Camera

```bash
yolo predict model=models/best.onnx source=0 show=True conf=0.5
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info |
| POST | `/detect` | JSON detection results |
| POST | `/detect/visual` | Annotated image |

## Project Structure
