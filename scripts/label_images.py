from ultralytics import YOLO
import os

def label_images(image_dir, label_dir):
    model = YOLO("yolov8n.pt")
    image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
    os.makedirs("runs/detect/predict/labels", exist_ok=True)

    for img in image_files:
        results = model.predict(f"{image_dir}/{img}", save_txt=True)
        label_file = img.replace(".jpg", ".txt")
        src_path = f"runs/detect/predict/labels/{label_file}"
        dest_path = f"{label_dir}/{label_file}"
        if os.path.exists(src_path):
            os.rename(src_path, dest_path)
        else:
            open(dest_path, "a").close()  # Empty label for no detections

    os.system("rm -rf runs/detect/predict")

if __name__ == "__main__":
    os.makedirs("data/labels", exist_ok=True)
    label_images("data/images", "data/labels")