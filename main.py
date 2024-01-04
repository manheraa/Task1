from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
  # load a pretrained model (recommended for training)

# Use the model
result=model.train(data="config.yaml", epochs=3)  # train the model
