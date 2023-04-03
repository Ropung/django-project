from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse,FileResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core import serializers
from json import loads
from .models import Order,Reply

def home(request):
    return HttpResponseRedirect("/order/")


# 따로 만든 url이 있다면 login_url 키워드를 지정해야한다.
def index(request):
    oList = None
    context = {}
    if "searchType" in request.GET and "searchWord" in request.GET:
        search_type = request.GET["searchType"]
        search_word = request.GET["searchWord"]

        # match (자바 스위치)
        if search_type == "order":
            oList = Order.objects.filter(order_text__contains=search_word).order_by(
                "order_text"
            )
        elif search_type == "address":
            oList = Order.objects.filter(address__contains=search_word).order_by(
                "-address"
            )
        elif search_type == "price":
            oList = Order.objects.filter(price__contains=search_word).order_by("price")
        # 검색 했을때만 검색 기준과 키워드를 context에 넣는다
        context["searchType"] = search_type
        context["searchWord"] = search_word
    else:
        oList = Order.objects.all().order_by("-id")

    # 페이징 넣기
    paginator = Paginator(oList, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    # Paginator 클래스를 이용해서 자른 목록의 단위에서 몇번째 단위를 보여줄 것인지 정한다
    context["page_obj"] = page_obj
    return render(request, "order/index.html", context)
    #


def read(request, id):
    order = Order.objects.get(id=id)
    # reply_list = Reply.objects.filter( order_obj = id ).order_by('-id')

    if request.method == "GET":
        context = {
            "o": order,
            "oList": order.order_text.split(","),
            # "reply_list":reply_list
            }
        return render(request, "order/read.html", context)


@login_required(login_url="common:login")
def write(request):
    if request.method == "GET":
        return render(request, "order/order_form.html")
    else:
        print(request.POST)
        print(request.FILES)
        if request.user:
            order = Order(
                order_text = request.POST["order_text"],
                address = request.POST["address"],
                price = request.POST["price"],
                author = request.user
            )
            # get 매서드 사용하는 이유
            # 딕셔너리에서 존재하지 않는 키를 딕셔너리[키] -> KeyError
            # 딕셔너리.get("키") -> None
            if request.FILES.get('uploadFile'):
                upload_file = request.FILES["uploadFile"]
                # 요청에 들어있던 첨부파일을 모델에 설정
                order.attached_file = upload_file
                order.original_file_name = upload_file.name
            order.save()
            return redirect("order:index")
        return redirect("order:index")


@login_required(login_url="common:login")
def update(request, id):
    o = Order.objects.get(id=id)
    if o.author.username != request.user.username:
        return redirect("/order/")
    if request.method == "GET":
        context = {"o": o }
        return render(request, "order/update.html", context)
    else:

        order_text = request.POST["order_text"]
        price = request.POST["price"]
        address = request.POST["address"]

        o.order_text = order_text
        o.price = price
        o.address = address

        print(request.FILES)
        if request.FILES.get('uploadFile'):
            print("오니?")
            upload_file = request.FILES["uploadFile"]
            o.attached_file = upload_file
            o.original_file_name = upload_file.name
        else :
            o.attached_file = None
            o.original_file_name = None
        o.save()

        context = {"o": o}
        return redirect("/order/" + str(id))


@login_required(login_url="common:login")
def delete(request, id):
    # 해당 객체 가져오기
    o = Order.objects.get(id=id)
    if o.author.username != request.user.username:
        return redirect("common:login")

    # 권한이 같을때 삭제 실행
    o.delete()

    return redirect("order/")


# @login_required(login_url="common:login")
def write_reply(request, id):
    user = request.user
    r = loads(request.body)
    print(r)
    reply_text = r['replyText']
    # reply_content = request.POST['reply_content']
    # &기존 방법
    # Reply.objects.create(
    #     user=user,
    #     reply_content = reply_content,
    #     order_obj = Order.object.get( id = id )
    # )
    # &queryset을 이용한 방법
    order = Order.objects.get(id = id)
    order.reply_set.create(
        reply_content = reply_text,
        user=user,
    )
    # return redirect("order:read" ,id)
    return JsonResponse({'result':'success'})


# @login_required(login_url="common:login")
def delete_reply(request, id):
    rid =(loads(request.body))['rid']
    Order.objects.get(id=id).reply_set.get(id = rid).delete()
    return JsonResponse({'data':"success"})

# @login_required(login_url="common:login")
def update_reply(request,id):
    if request.method == "GET" :
        rid = request.GET['rid']
        reply = Order.objects.get(id=id).reply_set.get(id = rid)
        context = {
            "id":reply.id,
            "reply_Text":reply.reply_content
        }
        return JsonResponse(context)
        # return render(request,'order/read.html',context)

    else :  #POST일떄
        # rid = request.POST['rid']
        request_body = loads(request.body)
        print(request.body)
        rid = request_body["rid"]
        reply_text = request_body['replyText']

        reply = Order.objects.get(id = id).reply_set.get(id = rid)
        reply.reply_content = reply_text
        reply.save()
        return JsonResponse({'result':'success'})
        # return redirect("/order/" + str(id))


def call_ajax(request) :
    print("성공한거같아요")
    print(request.POST)
    # JSON.stringify 하면 아래 표현 사용할 수 없음
    # print(request.POST['txt'])
    data = loads(request.body) # dict형식으로 바꿔줌
    print('템플릿에서 보낸 데이터',data)
    # 에시) 꺼낼때 키로 꺼냄
    output_key = data['txt']
    return JsonResponse({'result':'ㅊㅋㅊㅋ'})

def load_reply(request , id):
    # reply_list = Reply.objects.filter( order = id )
    reply_list = Order.objects.get( id = id ).reply_set.all()

    reply_dict_list=[]
    #reply_list의 정보를 가지고 dictionary만들기
    for r in reply_list:
        reply_dict ={
            'id': r.id,
            'username':r.user,
            'replyText': r.reply_content,
            'inputDate': r.input_date,
        }
        reply_dict_list.append(reply_dict)
    # serialized_list = serializers.serialize('json',reply_list)
    return JsonResponse({'replyList': reply_dict_list})

def download(request,id) :
    print(id)
    order = Order.objects.get(id=id)
    attached_file = order.attached_file
    original_file_name= order.original_file_name
    # 글번호에 달려있던 첨부파일로 파일형식 응답 객체생성
    response =  FileResponse(attached_file)
    response["Content-Disposition"] = 'attachment; filename=%s' %original_file_name

    return response