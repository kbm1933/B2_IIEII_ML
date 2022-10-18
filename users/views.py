from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession  # 이름이 같은 login이 있으니 as로 정의된 loginsession 으로 변수이름 설정 가능
from django.shortcuts import get_object_or_404  # 404페이지를 띄우기 위한 import


def signup(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'signup.html')   # render는 html 페이지 보여주겠다는 의미
    elif request.method == 'POST':  # 회원가입 진행 
        username = request.POST.get('username')   # username은 signup.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        profile = request.POST.get('profilefromfront') # profilefromfront 작성된 내용이 profile에 저장
        passwordcheck = request.POST.get('passwordcheck')

        if password == passwordcheck:
            User.objects.create_user(username=username, password=password, profile=profile)  # models에 저장되어있는 User에 내가 만든 user 저장 (암호화를 곁들인) + profile=profile 은 models에서의 key값과 17번 줄의 변수값을 비교하는 것 (같은변수 아님)
            return HttpResponse('회원가입 완료')
        else:
            # 안좋은 코드
            return HttpResponse('비밀번호가 틀렸습니다')

        return HttpResponse('다른 페이지')




def login(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'login.html')
    elif request.method == 'POST':  # 로그인 요청
        username = request.POST.get('username')    # username은 login.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

    #로그인 GET or POST 작업 후 이 다음코드 진행

        if user is not None:  # user 가 존재하지 않는게 아니면 = if user (user 라면!)
            # 장고에서 제공해주는 login 기능을 as로 재정의 후 이용
            loginsession(request, user)
            return redirect('community:fileupload')   #로그인 성공시 입력된 user 값으로 로그인 흐 user/ 로 경로이동
        else:
            return redirect('users:login')