import os
import cv2
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
    imgmodel = FileUpload.objects.get(id=idx)

# ==================================================================================================
# 첫 번째 방법 : opencv RGB 문제로 ex)키위를 블루베리라고 인식 하는데 이미지와 테두리는 깔끔하게 나옴
#     url = imgmodel.imgfile # 입력된 사진의 url
#     img = cv2.imread(url) # url을 이용해서 사진을 nparray로 바꿔주기
#     results = model(img)
#     detect = results.pandas().xyxy[0]  # 좌표 얻기
#     print(detect)
#     results.save()
#     cv2.imwrite(f'media/YOLO/result{idx}.jpg', img)

# 두 번째 방법 : rgb 재배열을 통해 사물을 잘 인식하지만 눈에 보이는 사진이 색이 바뀌어있음
#     url = imgmodel.imgfile # 입력된 사진의 url
#     img = cv2.imread(url) # url을 이용해서 사진을 nparray로 바꿔주기
#
#     b, g, r = cv2.split(img)   # img파일을 b,g,r로 분리
#     img = cv2.merge([r,g,b])   # 재배열
#
#     results = model(img)
#     detect = results.pandas().xyxy[0]  # 좌표 얻기
#     print(detect)
#     results.save()
#     cv2.imwrite(f'media/YOLO/result{idx}.jpg', img)

# 세 번째 방법 : PIL IMAGE 모듈을 통해 이미지를 가져오는 방법. 색이 그대로 나오고 사물인식도 잘 되지만 테두리가 없음
    img_bytes = imgmodel.imgfile.read()
    img = im.open(io.BytesIO(img_bytes)) #jpg로 파일 open

    img2= np.array(img) #jpg >> numpy array로 변경

    results = model(img2)
    detect = results.pandas().xyxy[0] #좌표 얻기
    print(detect)
    results.save()

    final_img = im.fromarray(img2) #numpy array >> jpg로 변경

    final_img.save(f'media/YOLO/result{idx}.jpg', "JPEG")
# ==================================================================================================

    yolo_url = (f'YOLO/result{idx}.jpg')

    detect_result = results.pandas().xyxy[0].to_numpy() # 인식한 결과의 정보 : 확률과 어떤 과일인지 클래스 이름
    print(detect_result)
    confidence = int(detect_result[0][4] * 100)
    fruit_cls = detect_result[0][6]

    YoloResult.objects.create(imgs=yolo_url, confidence=confidence, fruit_class=fruit_cls)
    return()
