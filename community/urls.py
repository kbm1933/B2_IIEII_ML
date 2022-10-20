from django.shortcuts import redirect
from django.urls import path
from community import views
from django.conf import settings


app_name = 'community'

# url 순서가 상관있을때가 있음..
urlpatterns = [
    path('fileupload/', views.fileUpload, name='fileupload'),
    path('file_result/', views.file_result, name='file_result'), 
    path('<int:file_id>/', views.detail_image_info, name='detail_image_info'),
    path('content_write/', views.content_write, name='content_write'),
    path('create_post', views.create_post, name='create_post'),
    path('fileupload/error/',views.fileUpload, name='error'),
] 