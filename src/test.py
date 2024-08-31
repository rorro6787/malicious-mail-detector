from ultralytics import YOLO    
import sys
import os


def detect_entities(image_path):
    # Load the model
    model = YOLO("yolov8s.pt", task="detect")

    # Perform inference
    results = model(image_path, save = True, project=os.path.dirname(image_path))
    # Results is a list of dictionaries, one for each detected object


if __name__ == '__main__':
    # sacamos el path del argumento recibido al programa
    image_path = sys.argv[1]
    print(detect_entities(image_path))




