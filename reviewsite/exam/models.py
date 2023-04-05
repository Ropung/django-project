from django.db import models
from django.utils import timezone

class Movie(models.Model):
    # 영화장르
    genre = models.CharField(max_length=20)
    # 영화이름
    movie_name =  models.CharField(max_length=100)
    # 영화내용
    movie_summary =  models.TextField()
    # 영화 등록일
    reg_date =  models.DateTimeField(default=timezone.now)

class Review(models.Model):
    # 리뷰 작성자
    reviewer_name =  models.CharField(max_length=20)
    # 영화 객체
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    # 리뷰 내용
    review_text =  models.TextField()
    # 영화 평점
    score =  models.IntegerField(default=0)
    # 리뷰 등록일
    reg_date =  models.DateTimeField(default=timezone.now)

