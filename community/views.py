from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.forms import FileUploadForm
from community.models import FileUpload
from django.shortcuts import get_object_or_404

# Create your views here.



def fileUpload(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'fileupload.html') 
    elif request.method == 'POST':
        title = request.POST.get('title')
        imgfile = request.FILES['file']
        user = request.user

        FileUpload.objects.create(user=user, title=title, imgfile=imgfile)

        return redirect('community:file_result')
    


def file_result(request):
    files = FileUpload.objects.all()

    context = {
        'files':files
    }

    return render(request, 'file_result.html', context)



def detail_image_info(request, file_id):
    # article = Article.objects.get(id=article_id)
    file = get_object_or_404(FileUpload, id=file_id)

    context = {
        'file':file
    }

    return render(request, 'detail_image_info.html', context)