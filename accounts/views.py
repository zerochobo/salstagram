from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def signup(request):
    if request.method == "POST":  # 요청 메서드가 포스트면 실행
        if request.POST["password"] == request.POST["password2"]:
            # 요청된 포스트 중 password 요소와 password2 요소가 같은지 검사
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password"])
            auth.login(request, user)
            # 참이면 유저를 요청된 메서드 중 username 과 password 를 이용하여 생성
            return render(request, 'accounts/signup_complete.html')
            # 유저 생성을 성공적으로 마치면 회원가입 성공 페이지로 이동
        return render(request, 'accounts/signup.html')
        # 일치하지 않으면 다시 회원가입 페이지로 이동
    return render(request, 'accounts/signup.html')

