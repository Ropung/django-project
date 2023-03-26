from django.db import models

# 데이터 베이스의 정보를 저장하는 객체
# ORM 방식으로 장고를 이용 할 때 필요한 클래스(java의 vo와 느낌이 비슷)
# django.db.models.Model 클래스를 상속받는 하위 클래스
# 모델객체를 생성하게 되면 장고에서 해당 모델에 대한 DB접근 API 자동으로 연결해줌

# 모델 - DB의 매핑 관계
# 장고모델 - Table
# 모델 속성 - Table column
# 모델 객체(1개) - Table row

#모델 선언
class Friend(models.Model):
    # 열선언
    #짧은 문자열에 대해서 CharField(최대 길이 필수) 사용 
    friend_name = models.CharField(max_length=10)
    # IntegerField() 정수
    friend_age = models.IntegerField()
    friend_bigo = models.TextField(null = True,blank=True)

