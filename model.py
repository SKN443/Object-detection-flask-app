import torch
from yolov5 import utils
import os
import shutil

def object_detection(url): 
    file_name = os.path.basename(url)
    command = f'''python3 yolov5/detect.py --weights yolov5s.pt --img 640 \
              --conf 0.25 --source {url} --name {file_name} \
              --hide-conf --line-thickness 3'''
    os.system(command)
    source_file = f"yolov5/runs/detect/{file_name}/{file_name}"
    destination_folder = "static/results/"
    os.system("rmdir /s /q " + destination_folder)
    shutil.copy(source_file, destination_folder)
    shutil.rmtree(f'yolov5/runs/detect/{file_name}')
    return f"results/result_{file_name}" 
