from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Order

def home(request):
    return HttpResponseRedirect('/order/')

def index(request):
    # -붙이면 DESC 안붙이면     
    oList = Order.objects.all().order_by('-id')
    return render(request,'order/index.html',{'oList':oList})
    # 
def find_order(request) :
    input_name = request.GET['find_order']
    option = request.GET['option']
    
    oList = []
    if  option == 'order':
        oList = Order.objects.filter(order_text__contains = input_name).order_by('order_text')
    elif option == 'address':
        oList = Order.objects.filter(address__contains = input_name).order_by('-address')
    elif option == 'front_address' :
        oList = Order.objects.filter(address__startswith = input_name ).order_by('address')
    elif option == 'price' :
        oList = Order.objects.filter(price__contains = input_name ).order_by('price')

    return render(request,'order/index.html',  {'oList' : oList})
    # 
def read(request, id):
    order = Order.objects.get(id = id)
    if request.method == "GET" :
        context = {
            'o' : order,
            "oList" : order.order_text.split(",")
            }
        return render(request,'order/read.html',context)
    # 
def write(request):
    if request.method == "GET" :
        return render(request,'order/order_form.html')
    else : 
        order_text = request.POST['order_text']
        address =request.POST['address']
        price =request.POST['price']
        
        Order.objects.create(
        order_text = order_text,
        price = price,
        address = address
        )
        
        return HttpResponseRedirect('/')
    # 
def update(request,id):
    o = Order.objects.get(id=id)

    if request.method == "GET" :
        context= {"o" : o}
        return render(request,'order/update.html',context)
    else :
        order_text = request.POST['order_text']
        price = request.POST['price']
        address =request.POST['address']

        o.order_text = order_text
        o.price = price
        o.address = address
        o.save()
        
        context= { "o" : o }
        return HttpResponseRedirect('/order/'+str(id))
    # 
def delete(request,id):
    Order.objects.get(id=id).delete()
    return HttpResponseRedirect('/')
# text
def logout(request):
    # 현재 세션정보의 user 라는 키를 가진 데이터 취득
    session_user = request.session.get('user')
    if session_user:
        print("로그아웃 성공")
        request.session['user'] = False
        return HttpResponseRedirect('/')
    elif not session_user :
        print("로그인 하슈")
        return HttpResponseRedirect('/login')
    print("logout >>> 예외처리")
    return  HttpResponseRedirect('/')
# 
def login(request):
    if request.method == "GET" :
        return render(request,'order/login.html')
    elif request.method == "POST" :
        user_id = request.POST["order_username"]
        user_pass = request.POST["order_password"]
        # FIXME user 테이블 조회 유효성 검사 or 토큰작업
        request.session['user'] = user_id
        return HttpResponseRedirect('/')
    print("login>>> 예외처리")
    return HttpResponseRedirect('/')