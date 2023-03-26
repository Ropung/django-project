from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def call1(request):
    template = loader.get_template('polls/template.html')
    print(request)
    context = {}
    return HttpResponse(template.render(context,request))

# RESTful 방식으로 호출된 주소에 대한 함수
# 요청 객체 뒤의 파라미터에 해당하는 변수명 써줘야함 
def call2(request, number ):
    print("number : ",number)
    
    template = loader.get_template('polls/template.html')
    print(request)
    context = {}
    return HttpResponse(template.render(context,request))

def call3(request):
    # request에서 가져오는 type은 str타입
    name = request.GET['name']
    age = request.GET['age']
    print("name : ",name)
    print("name : ",name)
    # template = __loader__.get_template('app/template.html')
    # print(request)
    context = {}
    return HttpResponse("호출됨")
# template.render(context,request)

def call4(request):
    template = loader.get_template('polls/template.html')
    print(request)
    context = {
        # 문자열하나 보내기
        'item' : 'This text is sent from server.',
        'name' : '홍길동',
        # 리스트 보내기
        'board_list':[
            {
                'title':'1등',
                'writer':'홍길동',
            },
            {
                'title':'1등',
                'writer':'김길동',
            },
            {
                'title':'1등',
                'writer':'고길동',
            },
        ],
        # 딕셔너리 보내기
        'mydata':{
            'name':'노기훈',
            'age':30,
            'address':'광주',
        },
    }

    return HttpResponse(template.render(context,request))

def call5(request):
    str_list = ['사과','딸기','바나나']
    str_list2 = []
    template = loader.get_template('polls/tag.html')
    print(request)
    context = {
      'list':str_list,
      'number':-3,
    }

    return HttpResponse(template.render(context,request))

def call6(request):
    template = loader.get_template('polls/form.html')
    print(request)
    context = {}
    return HttpResponse(template.render(context,request))

# 폼에 입력된 데이터 가져오기
def call_submit(request):
    name = request.POST['name']
    age = request.POST['age']
    print(name,age)
    return HttpResponse("submit OK")

# 선생님 과제
def call7(request):
    template = loader.get_template('polls/call7.html')
    name = "홍길동"
    age = 30
    addr= "서울"
    context = {
        "name":name,
        "age":age,
        "addr":addr,
    }
    return HttpResponse(template.render(context,request))
