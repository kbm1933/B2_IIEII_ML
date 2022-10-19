from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.forms import FileUploadForm
from community.models import FileUpload, YoloResult
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from yolo_code import detect
import cv2


# Create your views here.


@login_required
def fileUpload(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'fileupload.html') 
    elif request.method == 'POST':
        title = request.POST.get('title')
        imgfile = request.FILES['file']
        user = request.user

        FileUpload.objects.create(user=user, title=title, imgfile=imgfile)
       
        last_save = FileUpload.objects.last()
        idx = last_save.id
        # print('+++++++++++++++++++++++++++++++++++++++++++',idx) ##id값 확인
        detect.get_img(idx)

        return redirect('community:file_result')
    



@login_required
def file_result(request):
    # files = FileUpload.objects.all()
    files = YoloResult.objects.all().order_by('-id')

    context = {
        'files':files
    }

    return render(request, 'file_result.html', context)




@login_required
def detail_image_info(request, file_id):
    # article = Article.objects.get(id=article_id)
    file = get_object_or_404(FileUpload, id=file_id)

    context = {
        'file':file
    }

    return render(request, 'detail_image_info.html', context)