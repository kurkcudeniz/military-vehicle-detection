"""
Askeri arac tespiti + ByteTrack ile coklu nesne takibi.

Her karede YOLOv8 araclari tespit eder, ByteTrack bu tespitleri
kareler arasinda eslestirip her araca kalici bir ID verir.

Kullanim:
    python src/video_detect.py <video_yolu.mp4>
"""

import sys
import time
from pathlib import Path

import cv2
from ultralytics import YOLO

if len(sys.argv) < 2:
    print("Kullanim: python src/video_detect.py <video_yolu.mp4>")
    sys.exit(1)

video_yolu = sys.argv[1]
model = YOLO("models/best.pt")

# Cikti videosu icin giris videosunun boyut ve fps bilgisini al
cap = cv2.VideoCapture(video_yolu)
genislik = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yukseklik = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_fps = cap.get(cv2.CAP_PROP_FPS) or 30
cap.release()

Path("results").mkdir(exist_ok=True)
cikti_yolu = "results/tracking_output.mp4"
yazici = cv2.VideoWriter(
    cikti_yolu,
    cv2.VideoWriter_fourcc(*"mp4v"),
    video_fps,
    (genislik, yukseklik),
)

gorulen_idler = set()   # Video boyunca gorulen tum farkli arac ID'leri
sureler = []            # Her karenin islenme suresi (ms)
kare_no = 0

print(f"{video_yolu} isleniyor (YOLOv8 + ByteTrack)...")

# stream=True: kareleri tek tek verir, tum videoyu bellege yuklemez
# persist=True: ID'ler kareler arasinda korunur
sonuclar = model.track(
    source=video_yolu,
    tracker="bytetrack.yaml",
    persist=True,
    stream=True,
    conf=0.3,
    verbose=False,
)

t_onceki = time.perf_counter()
for sonuc in sonuclar:
    t_simdi = time.perf_counter()
    sureler.append((t_simdi - t_onceki) * 1000)
    t_onceki = t_simdi

    if sonuc.boxes.id is not None:
        for arac_id in sonuc.boxes.id.int().tolist():
            gorulen_idler.add(arac_id)

    # plot(): kutulari, sinif adini, guveni ve takip ID'sini cizer
    cizili_kare = sonuc.plot()
    yazici.write(cizili_kare)
    kare_no += 1

yazici.release()

# Ilk 10 kare isinma (warmup), ortalamaya katma
olcum = sureler[10:] if len(sureler) > 20 else sureler
ort_ms = sum(olcum) / len(olcum)

print("\nIslem tamam.")
print(f"Toplam kare        : {kare_no}")
print(f"Farkli arac sayisi : {len(gorulen_idler)}  (ID'ler: {sorted(gorulen_idler)})")
print(f"Ortalama sure      : {ort_ms:.1f} ms/kare  ->  {1000 / ort_ms:.1f} FPS")
print(f"Cikti videosu      : {cikti_yolu}")
