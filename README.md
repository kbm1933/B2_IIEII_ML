# IIEII 사물 인식 프로젝트 #
## **프로젝트 개요**
- [실전 머신러닝]을 실습 하며 배운 머신러닝 기반으로 사물 분류 웹서비스 개발


## 목표
- Django와 머신러닝을 활용하여 기한 내에 프로젝트 완성을 목표
- CNN/YOLO를 이용하여 이미지 분할(Segmentation)하는 과정 이해


## ⏲️ 개발기간
2022년 10월 17일 ~ 2022년 10월 20일


## 🧙 멤버구성
팀장 [김병문](https://github.com/kbm1933)
팀원 [김동익](https://github.com/DongIkkk), [오형석](https://github.com/auberr), [이혜원](https://github.com/wonprogrammer), [최정윤](https://github.com/uniqquej)


## 주요 구현 기능
- 핵심 기능
    - 머신러닝
        - [사물 인식] 업로드 된 사진이 과일인지 아닌지 분류
        - 과일로 분류된 사진은 어떤 과일인지 분류
    - 장고
        - 사진 파일 업로드 기능 구현
        - 업로드된 사진 클릭하면 페이지 이동, 해당 이미지 카테고리 출력


## 주요 구현 방법
- 머신러닝
   - 사용한 데이터셋
        [Fruit 360 | Kaggle | Dataset](https://www.kaggle.com/datasets/moltean/fruits)

  - 사용한 라벨링 툴
        [Label Studio](https://github.com/heartexlabs/labelImg)

   - 사용한 머신러닝(딥러닝) 모델
        [YOLOv5](https://github.com/ultralytics/yolov5)

   - 라벨링한 데이터를 학습한 컴퓨터
        [Colab notebooks](https://colab.research.google.com/)

- 장고
  - django 

## 프로젝트 소개 상세 노션 페이지
[상세보기](https://onyx-linen-fe0.notion.site/IIEII-84598579ff8e447ba3c44949792673d6)



## 프로젝트 진행상황

- 10/17(월)
    - 머신러닝 : 학습할 데이터 라벨링
    [김병문](https://github.com/kbm1933), [김동익](https://github.com/DongIkkk), [오형석](https://github.com/auberr), [최정윤](https://github.com/uniqquej)
        - [YOLOv5](https://github.com/ultralytics/yolov5) 모델을 사용해서 11가지 과일을 학습 사용
        - [Fruits 360](https://www.kaggle.com/datasets/moltean/fruits) 데이터 셋을 사용
        - 11가지 과일을 선별해서 [라벨링](https://github.com/heartexlabs/labelImg)
        - blueberry, grape, kiwi, lemon, mango, melon, peach, pear, pineapple, strawberry, watermelon

    - 장고 : 사용자가 업로드한 파일 database에 업로드 한 뒤 가져오기 [이혜원](https://github.com/wonprogrammer)
         - 미해결 : 이미지 저장 및 호출은 되는데 사진으로 불러와지는게 아니라 경로'주소'가 불러와짐 
         
- 10/18(화)
    - 머신러닝 : 사물 인식_모델 테스트 및 학습
    [김병문](https://github.com/kbm1933), [김동익](https://github.com/DongIkkk), [오형석](https://github.com/auberr), [최정윤](https://github.com/uniqquej)

    - 장고 : 미해결 부분 이미지 태그와 DTL사용해서 해결완료 [이혜원](https://github.com/wonprogrammer)
    - 장고 : 로그인 로그아웃 기능 + 로그인된 사용자만 community templates에 접근가능

- 10/19(수)
    - 머신러닝 및 장고 : 학습한 모델을 장고 내 작동 구현
        [김병문](https://github.com/kbm1933), [김동익](https://github.com/DongIkkk), [오형석](https://github.com/auberr), [이혜원](https://github.com/wonprogrammer), [최정윤](https://github.com/uniqquej)


- 10/20(목)
    - 머신러닝 및 장고 : 장고 css 추가 및 기능보완
    - 장고 : 게시글 작성 완성
