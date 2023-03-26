from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Board

def home(request):
    return HttpResponseRedirect('/board/')


def index(request):
    # -붙이면 DESC 안붙이면 
    board_list = Board.objects.all().order_by('-id')

    context ={
        'board_list':board_list
    }
    return render(request,'board/index.html',context)

def read(request, id):

    board = Board.objects.get(id = id)
    board.view_count += 1
    board.save()

    if request.method == "GET" :
        context = {'board' : board}
        return render(request,'board/read.html',context)
    # elif request.method == "POST" :
    #     friend.friend_name = request.POST['friend_name']
    #     friend.save()
    #     return HttpResponseRedirect('/friend/show_all/')

def write(request):
    
    if request.method == "GET" :
        return render(request,'board/board_form.html')
    else : 
        title = request.POST['title']
        content =request.POST['content']
        
        # 현재 세션정보의 writher 라는 키를 가진 데이터 취득
        session_writer = request.session.get('writer')
        if not session_writer:
            request.session['writer'] = request.POST['writer']
       
        Board.objects.create(
        title = title,
        writer = request.session.get('writer'),
        content = content
        )
        return HttpResponseRedirect('/')

def update(request,id):
    b = Board.objects.get(id=id)

    if request.method == "GET" :
        context= {"b" : b}
        return render(request,'board/update.html',context)
    else :
        title = request.POST['title']
        writer = request.POST['writer']
        content =request.POST['content']

        b.title = title
        b.writer = writer
        b.content = content
        b.save()
        
        context= { "b" : b }
        return HttpResponseRedirect('/board/'+str(id))
    
def delete(request,id):
    Board.objects.get(id=id).delete()
    return HttpResponseRedirect('/')


# def add_friend(request):
#     t = loader.get_template('friend/friendForm.html')
#     context = {}

#     if request.method == "GET" :
#         return HttpResponse(t.render(context,request))
    
#     elif request.method == "POST" :
#         name = request.POST['friend_name']
#         age = request.POST['friend_age']
#         bigo = request.POST['friend_bigo']
#         f = Friend(
#             friend_name = name,
#             friend_age = age,
#             friend_bigo = bigo
#         )
#         f.save()
#         # 템플릿 반환 방식(단축) render(요청, 템플릿경로[ , context])
#         return HttpResponseRedirect('/friend/')
    
#     return HttpResponse(request.method)

# def create_friend(request):
#     t = loader.get_template('/friend/friendForm.html')
#     context = {}

#     if request.method == "GET" :
#         return HttpResponse(t.render(context,request))
    
#     elif request.method == "POST" :
#         name = request.POST['friend_name']
#         age = request.POST['friend_age']
#         bigo = request.POST['friend_bigo']
        
#         print(name,age,bigo)

#         #create()
#         Friend.objects.create(
#             friend_name = name,
#             friend_age = age,
#             friend_bigo = bigo
#         )
#         # 단축 방식으로 index.html rendering
#         return HttpResponseRedirect('/friend/show_all')
    
#     return HttpResponseRedirect('/friend/')

# def show_all(request) :
#     fList = Friend.objects.all()
#     context = {
#         'fList' : fList,
#     }
#     return render(request,'friend/friend_list.html',context)

# def find_friend(request) :
#     input_name = request.GET['friend_name']
#     condition = request.GET['condition']

#     fList = []
#     if condition == 'all' :
#         fList = Friend.objects.filter(friend_name = input_name)
#     else :
#         fList = Friend.objects.filter(friend_name__contains = input_name)

#     context = {
#             'fList' : fList,
#     }
 
#     return render(request,'friend/friend_list.html',context)

# def delete_friend(request,id) :
#     Friend.objects.get(id=id).delete()

#     return HttpResponseRedirect('/friend/show_all/')

# def update_friend(request,id) :
#     friend = Friend.objects.get(id = id)

#     if request.method == "GET" :
#         context = {'friend' : friend}
#         return render(request,'friend/friend_update.html',context)
#     elif request.method == "POST" :
#         friend.friend_name = request.POST['friend_name']
#         friend.friend_age = request.POST['friend_age']
#         friend.friend_bigo = request.POST['friend_bigo']
#         friend.save()
#         return HttpResponseRedirect('/friend/show_all/')