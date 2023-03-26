from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Friend

def index(request):
    t = loader.get_template('friend/index.html')
    context ={}
    return HttpResponse(t.render(context,request))

def add_friend(request):
    t = loader.get_template('friend/friendForm.html')
    context = {}

    if request.method == "GET" :
        return HttpResponse(t.render(context,request))
    
    elif request.method == "POST" :
        name = request.POST['friend_name']
        age = request.POST['friend_age']
        bigo = request.POST['friend_bigo']
        #save()
        f = Friend(
            friend_name = name,
            friend_age = age,
            friend_bigo = bigo
        )
        f.save()
        # 템플릿 반환 방식(단축) render(요청, 템플릿경로[ , context])
        return HttpResponseRedirect('/friend/')
    
    return HttpResponse(request.method)

def create_friend(request):
    t = loader.get_template('/friend/friendForm.html')
    context = {}

    if request.method == "GET" :
        return HttpResponse(t.render(context,request))
    
    elif request.method == "POST" :
        name = request.POST['friend_name']
        age = request.POST['friend_age']
        bigo = request.POST['friend_bigo']
        
        print(name,age,bigo)

        #create()
        Friend.objects.create(
            friend_name = name,
            friend_age = age,
            friend_bigo = bigo
        )
        # 단축 방식으로 index.html rendering
        return HttpResponseRedirect('/friend/show_all')
    
    return HttpResponseRedirect('/friend/')

def show_all(request) :
    fList = Friend.objects.all()
    context = {
        'fList' : fList,
    }
    return render(request,'friend/friend_list.html',context)

def find_friend(request) :
    input_name = request.GET['friend_name']
    condition = request.GET['condition']

    fList = []
    if condition == 'all' :
        fList = Friend.objects.filter(friend_name = input_name)
    else :
        fList = Friend.objects.filter(friend_name__contains = input_name)

    context = {
            'fList' : fList,
    }
 
    return render(request,'friend/friend_list.html',context)

def delete_friend(request,id) :
    Friend.objects.get(id=id).delete()

    return HttpResponseRedirect('/friend/show_all/')

def update_friend(request,id) :
    friend = Friend.objects.get(id = id)

    if request.method == "GET" :
        context = {'friend' : friend}
        return render(request,'friend/friend_update.html',context)
    elif request.method == "POST" :
        friend.friend_name = request.POST['friend_name']
        friend.friend_age = request.POST['friend_age']
        friend.friend_bigo = request.POST['friend_bigo']
        friend.save()
        return HttpResponseRedirect('/friend/show_all/')