from ultralytics import YOLO
import sys

if len(sys.argv) < 2:
    print("Kullanım: python src/video_detect.py <video_yolu.mp4>")
    sys.exit(1)

video_path = sys.argv[1]
model = YOLO('models/best.pt')

print(f"{video_path} işleniyor...")
results = model.predict(source=video_path, save=True, project="results", name="video_output", exist_ok=True)
print("İşlem tamam! Çıktı 'results/video_output' klasörüne kaydedildi.")
