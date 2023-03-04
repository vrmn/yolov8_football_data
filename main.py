import ultralytics
from ultralytics import YOLO
ultralytics.checks()

# from roboflow import Roboflow
# rf = Roboflow(api_key="k2MJLS6IomGjAxqLGSKv")
# project = rf.workspace("sathish-p-dqejw").project("football-players-detection-k8klx")
# dataset = project.version(2).download("yolov8")


# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

results = model.train(data="football-players-detection-2/data.yaml", epochs=30)  # train the model
# results = model.train(data="coco128.yaml", epochs=3)  # train the model


