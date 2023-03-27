from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator

def index(request):
    #아까 만든 common/index.html을 표시하고
    #local8000으로 들어갔을 때
    #잘 표시가 되는지 확인
    context ={}
    return render(request,'common/index.html',context)
