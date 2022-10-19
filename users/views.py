from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession  # 이름이 같은 login이 있으니 as로 정의된 loginsession 으로 변수이름 설정 가능
from django.shortcuts import get_object_or_404  # 404페이지를 띄우기 위한 import
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def signup(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'signup.html')  
    elif request.method == 'POST':  # 회원가입 진행 
        username = request.POST.get('username')   # username은 signup.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        profile = request.POST.get('profilefromfront') # profilefromfront 작성된 내용이 profile에 저장
        passwordcheck = request.POST.get('passwordcheck')

        if password == passwordcheck:
            User.objects.create_user(username=username, password=password, profile=profile) 
            return redirect('users:login')
        else:
            return render(request, 'signup.html')




def login(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'login.html')

    elif request.method == 'POST':  # 로그인 요청
        username = request.POST.get('username')    
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

    #로그인 GET or POST 작업 후 이 다음코드 진행

        if user is not None:  
            loginsession(request, user)
            return redirect('community:fileupload') 
        else:
            return redirect('users:login')



@login_required
def logout(request):
    auth.logout(request)
    return redirect('users:login')
