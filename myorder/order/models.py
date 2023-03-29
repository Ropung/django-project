from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #auth_user 테이블과 매핑되는 모델

# 데이터 베이스의 정보를 저장하는 객체
# ORM 방식으로 장고를 이용 할 때 필요한 클래스(java의 vo와 느낌이 비슷)
# django.db.models.Model 클래스를 상속받는 하위 클래스
# 모델객체를 생성하게 되면 장고에서 해당 모델에 대한 DB접근 API 자동으로 연결해줌

# 모델 - DB의 매핑 관계
# 장고모델 - Table
# 모델 속성 - Table column
# 모델 객체(1개) - Table row

#모델 선언
class Order(models.Model):
    # 번호는 pk 설정 안하면 장고가 자동으로 id 부여해줌
    ### 필드와 필드 사이에 컴마 금지 ###

    #상품
    order_text = models.CharField(max_length=100)
    # 가격
    price =  models.IntegerField(default=0 , blank=True, null=False)
    # 주소
    address = models.CharField(max_length=100)
    # 작성일
    order_date = models.DateTimeField(default=timezone.now)
    # 글쓴이
    # ForeignKey: 참조키, CASCADE:종속
    # db에는 필드이름_본키이름으로 열이 생성됨
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # 자바의 String 이랑 비슷하게
    # 객체 정보를 문자열로 돌려줌
    def __str__(self):
        # 밑에 두개는 같은표현
        # return "{}:{}".format(self.id,self.order_text)
        return f'{self.id} ~ {self.order_text} ~'

    # 모델스 패키지 상속받음
    # 댓글 정보를 포함하는 모델
class Reply(models.Model):
    #pk
    #게시글 번호(fk)
    order_obj = models.ForeignKey(Order,on_delete=models.CASCADE)
    #사용자(fk)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #덧글내용 content
    reply_content = models.TextField(null = False,blank=False)
    #작성시간
    input_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reply_content