from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# 커스텀 회원가입폼
from .forms import UserForm , CustomChangeForm

def index(request):
    #아까 만든 common/index.html을 표시하고
    #local8000으로 들어갔을 때
    #잘 표시가 되는지 확인
    context ={}
    return render(request,'common/index.html')

def signup_custom(request):

    if request.method == "POST" :
        print(request.POST)
        # request.POST에 들어있는 정보를 UserForm형식으로 변환
        form = UserCreationForm(request.POST)
    
        # 폼내용이 유효하다면
        if form.is_valid():
            #db에 폼정보 저장
            form.save() 
            # 폼에 입력한 값 가져오기
            username = form.cleaned_data.get('username')
            # 날것의 패스워드
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            # 인증하는 함수
            user = authenticate(
                username = username,
                password = raw_password,
                first_name = first_name,
                last_name = last_name
                )
            
            login(request,user)
            # 로그인 하고 메인 페이지로 넘김
            return redirect('/')
    else : # GET 방식으로 요청이 오면 비어있는 사용자 생성 폼을 만든다.
        form = UserCreationForm()
    return render(request,'common/signup.html',{'form':form})

@login_required(login_url='common:login')
def update(request):
    if not request.user.is_authenticated :
        return redirect('common:login')
    if request.method == "GET" :
        # CustomChangeForm(instance) 보내면 장고가 제공하는 기본 폼 사용 할 수 있음
        form = CustomChangeForm()
        return render(request,'common/update.html',{'form':form})
    else : #POST 일떄
        form = CustomChangeForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
        return redirect('common:index')

@login_required(login_url='common:login')
def delete(request):
    if not request.user.is_authenticated :
        return redirect('common:login')
    request.user.delete()
    # render나 redirect의 파라미터로 app_name:url_name 작성가능
    return redirect('common:index')