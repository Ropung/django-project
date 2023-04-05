from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from json import loads
from .models import Movie,Review


# 따로 만든 url이 있다면 login_url 키워드를 지정해야한다.
def index(request):
    mList = None
    context={}
    #리플순 정렬
    if "review_movie" in request.GET:
      print("타라")
      mList = Movie.objects.all().order_by("review_set.all")
      context['mList'] = mList
      return render(request, "exam/index.html",context)

    # 선택된 카테고리를 보여줌
    if "genreType" in request.GET :
        search_genre = request.GET["genreType"]
        if search_genre == "all":
            mList = Movie.objects.all().order_by("-id")
        if search_genre == "act":
            mList = Movie.objects.filter(genre__contains=search_genre).order_by("-id")
        elif search_genre == "ani":
            mList = Movie.objects.filter(genre__contains=search_genre).order_by("-id")
        elif search_genre == "comic":
            mList = Movie.objects.filter(genre__contains=search_genre).order_by("-id")
        # 검색 했을때만 검색 기준과 키워드를 context에 넣는다
        context["searchType"] = search_genre
        context['mList'] = mList
    else:
      mList = Movie.objects.all().order_by("-id")
      # mList = Movie.objects.all().order_by("-id")
      context['mList'] = mList
    return render(request, "exam/index.html",context)


def read(request, id):
    movie = Movie.objects.get(id=id)
    review_list = Review.objects.filter( movie = id ).order_by('-id')

    if request.method == "GET":

        score_sum = 0
        context={}

        if review_list :
          for r in review_list :
            score_sum += r.score
          score_average = score_sum / review_list.count()
        else :
          score_average = 0
        context = {
            "m": movie,
            "rList":review_list,
            'score_average': round(score_average)
            }
        return render(request, "exam/read.html", context)


def write(request):
    if request.method == "GET":
        return render(request, "exam/exam_form.html")
    else:

        m = Movie(
            genre = request.POST["genreType"],
            movie_name = request.POST["movie_title"],
            movie_summary = request.POST["movie_content"],
        )
        m.save()
        return redirect("exam:index")


def update(request, id):
    m = Movie.objects.get(id=id)
    if request.method == "GET":
        context = {"m": m }
        return render(request, "exam/update.html", context)
    else:
        m.genre = request.POST["genreType"]
        m.movie_name =  request.POST["movie_title"]
        m.movie_summary =  request.POST["movie_content"]
        m.save()
        context = {"m": m}
        return redirect("/"+str(id))

def delete(request, id):
    m = Movie.objects.get(id=id)
    m.delete()
    return JsonResponse({'data': id})

def write_review(request, id):
    r = loads(request.body)
    reviewer_name = r['r_viewer']
    review_text = r['r_text']
    score = r['r_score']
    m = Movie.objects.get(id = id)
    m.review_set.create(
        reviewer_name = reviewer_name,
        review_text = review_text,
        score = score
    )
    # 현재 세션에 리뷰어 등록
    request.session['reviewer'] = r['r_viewer']

    context = {
      'message': '댓글을 작성을 성공했습니다.',
    }

    return JsonResponse(context)


# # @login_required(login_url="common:login")
# def delete_reply(request, id):
#     rid =(loads(request.body))['rid']
#     Order.objects.get(id=id).reply_set.get(id = rid).delete()
#     return JsonResponse({'data':"success"})

# # @login_required(login_url="common:login")
# def update_reply(request,id):
#     if request.method == "GET" :
#         rid = request.GET['rid']
#         reply = Order.objects.get(id=id).reply_set.get(id = rid)
#         context = {
#             "id":reply.id,
#             "reply_Text":reply.reply_content
#         }
#         return JsonResponse(context)
#         # return render(request,'order/read.html',context)

#     else :  #POST일떄
#         # rid = request.POST['rid']
#         request_body = loads(request.body)
#         print(request.body)
#         rid = request_body["rid"]
#         reply_text = request_body['replyText']

#         reply = Order.objects.get(id = id).reply_set.get(id = rid)
#         reply.reply_content = reply_text
#         reply.save()
#         return JsonResponse({'result':'success'})
#         # return redirect("/order/" + str(id))


# def call_ajax(request) :
#     print("성공한거같아요")
#     print(request.POST)
#     # JSON.stringify 하면 아래 표현 사용할 수 없음
#     # print(request.POST['txt'])
#     data = loads(request.body) # dict형식으로 바꿔줌
#     print('템플릿에서 보낸 데이터',data)
#     # 에시) 꺼낼때 키로 꺼냄
#     output_key = data['txt']
#     return JsonResponse({'result':'ㅊㅋㅊㅋ'})

# def load_reply(request , id):
#     # reply_list = Reply.objects.filter( order = id )
#     reply_list = Order.objects.get( id = id ).reply_set.all()

#     reply_dict_list=[]
#     #reply_list의 정보를 가지고 dictionary만들기
#     for r in reply_list:
#         reply_dict ={
#             'id': r.id,
#             'username':r.user,
#             'replyText': r.reply_content,
#             'inputDate': r.input_date,
#         }
#         reply_dict_list.append(reply_dict)
#     # serialized_list = serializers.serialize('json',reply_list)
#     return JsonResponse({'replyList': reply_dict_list})

