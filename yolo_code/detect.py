import os
import cv2
import torch
import pandas
import django
from community.models import FileUpload,YoloResult
# from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wetyle_share.settings')
django.setup()


def get_img(idx):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolo_code/last.pt', force_reload=True)
    imgmodel = FileUpload.objects.get(id=idx)
    url = imgmodel.imgfile #입력된 사진의 url
    img = cv2.imread(url) #url을 이용해서 사진을 nparray로 바꿔주기
    results = model(img)
    detect = results.pandas().xyxy[0] #좌표 얻기
    print(detect)
    results.save()

    cv2.imwrite(f'media/YOLO/result{idx}.jpg', img)
    yolo_url = (f'YOLO/result{idx}.jpg')

    detect_result = results.pandas().xyxy[0].to_numpy() # 인식한 결과의 정보 : 확률과 어떤 과일인지 클래스 이름
    print(detect_result)
    confidence = detect_result[0][4] * 100
    fruit_cls = detect_result[0][6]

    YoloResult.objects.create(imgs=yolo_url, confidence=confidence, fruit_class=fruit_cls)
    return()
