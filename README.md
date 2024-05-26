# Object detection image app
This is a flask application for object detection on uploaded image using [YOLOv5](https://github.com/ultralytics/yolov5/tree/master).

## Getting Started
To run app locally, follow these steps:

### 1. Clone the repository to your local machine.
```bash
git clone https://github.com/SKN443/Object-detection-flask-app.git
cd Object-detection-flask-app
```

### 2. Set up virtual environment
```bash
python -m pip install virtualenv
```

### 3. Create and activate venv
```bash
python -m venv myenv
myenv/Scripts/activate  
```
Above line is for Window. Using `source myenv/bin/activate` to activate virtual environment in Ubuntu.

### 4. Install [YOLOv5](https://github.com/ultralytics/yolov5/tree/master)
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -qr requirements.txt comet_ml
```

### 5. Install Flask module and run your local app
```bash
pip install flask
cd ..
python app.py
```

Access the application in your web browser at `http://127.0.0.1:5000/`
