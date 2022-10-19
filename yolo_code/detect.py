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
 

    cv2.rectangle(img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (0,0,255))
    cv2.imwrite(f'result{idx}.png', img)
    
    yolo_url = (f'D:/prog/B2_IIEII_ML/result{idx}.png')
   
    YoloResult.objects.create(imgs = yolo_url)
    
    return()