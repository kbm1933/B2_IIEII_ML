from django.shortcuts import redirect
from django.urls import path
from community import views


app_name = 'community'

# url 순서가 상관있을때가 있음..
urlpatterns = [
    path('fileupload/', views.fileUpload, name='fileupload'),
    path('file_result/', views.file_result, name='file_result'), 
    path('<int:file_id>/', views.detail_image_info, name='detail_image_info'),
] 