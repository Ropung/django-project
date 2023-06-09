from django.db import models
from django.utils import timezone

# 데이터 베이스의 정보를 저장하는 객체
# ORM 방식으로 장고를 이용 할 때 필요한 클래스(java의 vo와 느낌이 비슷)
# django.db.models.Model 클래스를 상속받는 하위 클래스
# 모델객체를 생성하게 되면 장고에서 해당 모델에 대한 DB접근 API 자동으로 연결해줌

# 모델 - DB의 매핑 관계
# 장고모델 - Table
# 모델 속성 - Table column
# 모델 객체(1개) - Table row

#모델 선언
class Board(models.Model):
    # 번호는 pk 설정 안하면 장고가 자동으로 id 부여해줌
    ### 필드와 필드 사이에 컴마 금지 ###
    # 제목
    
    title = models.CharField(max_length=100)
    # 내용
    content = models.TextField()
    # 글쓴이
    writer = models.CharField(max_length=10)
    # 작성일
    input_date = models.DateTimeField(default=timezone.now)
    #조회수
    view_count = models.IntegerField(default=0) 
