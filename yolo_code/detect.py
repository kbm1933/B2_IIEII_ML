import os
import torch
import pandas
import django
from community.models import FileUpload,YoloResult
from PIL import Image as im
import numpy as np
import io
# from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wetyle_share.settings')
django.setup()


def get_img(idx):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolo_code/last.pt', force_reload=True)
    imgmodel = FileUpload.objects.get(id=idx) #업로드 한 이미지

    img_bytes = imgmodel.imgfile.read()
    img = im.open(io.BytesIO(img_bytes)) #jpg로 파일 open

    img2= np.array(img) #jpg >> numpy array로 변경

    results = model(img2)
    detect = results.pandas().xyxy[0] #좌표 얻기
    print(detect)
    results.save()

    final_img = im.fromarray(img2) #numpy array >> jpg로 변경

    final_img.save(f'media/YOLO/result{idx}.jpg', "JPEG")

    yolo_url = (f'YOLO/result{idx}.jpg')

    detect_result = results.pandas().xyxy[0].to_numpy() # 인식한 결과의 정보 : 확률과 어떤 과일인지 클래스 이름
    print(detect_result)
    confidence = int(detect_result[0][4] * 100)
    fruit_cls = detect_result[0][6]

    YoloResult.objects.create(imgs=yolo_url, confidence=confidence, fruit_class=fruit_cls)
    return()
