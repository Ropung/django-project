from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

def index(request):
    #아까 만든 common/index.html을 표시하고
    #local8000으로 들어갔을 때
    #잘 표시가 되는지 확인
    context ={}
    return render(request,'common/index.html')

def signup(request):

    if request.method == "POST" :
        # 요청 객체가 담고있는 정보로 사용자 생성 폼을 만든다.
        print(request.POST)
        form = UserCreationForm(request.POST)
        # 폼내용이 유효하다면
        if form.is_valid():
            #db에 폼정보 저장
            form.save() 
            # 폼에 입력한 값 가져오기
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username = username,password = raw_password)
            login(request,user)
            return redirect('/')
    else :
        # GET 방식으로 요청이 오면 비어있는 사용자 생성 폼을 만든다.
        form = UserCreationForm()
    return render(request,'common/signup.html',{'form':form})