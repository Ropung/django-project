from django import forms
from django.contrib.auth.forms import UserChangeForm ,UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = forms.CharField
    last_name = forms.CharField
    #폼의 정보를 담고 있는 내부 클래스
    class Meta: 
        model = User
        fields = ("username","email","first_name","last_name")
        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password' : forms.PasswordInput(attrs={'class': 'form-control'}),}
        # labels = {
        #     'username': '닉네임',
        #     'email': '이메일',
        #     'password': '패스워드',
        #     'first_name': '성',
        #     'last_name': '이름',
        # }
class CustomChangeForm(UserChangeForm):
    class Meta :
        model = User
        fields = ("email","first_name","last_name")