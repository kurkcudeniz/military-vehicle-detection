from ultralytics import YOLO
import cv2
import argparse
import os

def detect(image_path, model_path="models/best.pt", conf=0.3):
    model = YOLO(model_path)
    results = model(image_path, conf=conf)
    
    detections = []
    for box in results[0].boxes:
        sinif = model.names[int(box.cls)]
        guven = round(float(box.conf) * 100, 1)
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        detections.append({
            "class": sinif,
            "confidence": guven,
            "bbox": [x1, y1, x2, y2]
        })
    
    # Sonucu kaydet
    annotated = results[0].plot()
    output_path = os.path.join("results", os.path.basename(image_path))
    cv2.imwrite(output_path, annotated)
    
    return detections, output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Military Vehicle Detection")
    parser.add_argument("image", help="Path to input image")
    parser.add_argument("--conf", type=float, default=0.3, help="Confidence threshold")
    args = parser.parse_args()
    
    detections, output = detect(args.image, conf=args.conf)
    print(f"\n{len(detections)} vehicle(s) detected:")
    for d in detections:
        print(f"  {d['class']}: {d['confidence']}%")
    print(f"\nResult saved to: {output}")
