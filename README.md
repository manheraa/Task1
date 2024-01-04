# Task1
#Install ultralytics module using pip install ultralytics.

#Create an custom yolov8 nano module and train the module using annoted data.
-We have to configure the model for training that is done using config.yaml file
-Run the model
-After training we predict the result using 
!yolo task=detect mode=predict model=/content/runs/detect/train12/weights/best.pt conf=0.25 source=/content/drive/MyDrive/task1/images/train #select the folder containing the testing images to make prediction
-The result will be stored in runs/detect folder.
