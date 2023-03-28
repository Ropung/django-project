from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Order
from django.core.paginator import Paginator

def home(request):
    return HttpResponseRedirect('/order/')

def index(request):

    oList = None
    context = {}
    if 'searchType' in request.GET and 'searchWord' in request.GET :
        search_type = request.GET['searchType']
        search_word = request.GET['searchWord']

        # match (자바 스위치)
        if  search_type == 'order':
            oList = Order.objects.filter(order_text__contains = search_word).order_by('order_text')
        elif search_type == 'address':
            oList = Order.objects.filter(address__contains = search_word).order_by('-address')
        elif search_type == 'price' :
            oList = Order.objects.filter(price__contains = search_word ).order_by('price')
        # 검색 했을때만 검색 기준과 키워드를 context에 넣는다
        context['searchType'] = search_type
        context['searchWord'] = search_word
    else :
        oList = Order.objects.all().order_by('-id')

    # 페이징 넣기
    paginator = Paginator(oList,10)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Paginator 클래스를 이용해서 자른 목록의 단위에서 몇번째 단위를 보여줄 것인지 정한다
    context['page_obj'] = page_obj
    return render(request,'order/index.html',context)
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
