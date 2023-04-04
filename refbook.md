- CharField(max_length=10) 짧은문자열 파라미터 길이필수
- IntegerField() 정수필드
- TextField(null = True,blank=True) 긴문자열 blank = 공백on/off
- null 과 blank의 차이
- null은 DB를 위한 항목, blank는 데이터 검증에 대한 항목
- primary_key = True << 해당 필드를 기본키로 지정
- default 필드의 기본값을 지정하는 옵션

- 마이그레이션 migration : 작성된 모델을 토대로 DB에 DDL을 실현
- 하위 앱을 setting.py에 등록 해야지 사용 할 수 있다.

1. (terminal): django-admin startapp friend 앱만들기
2. (make): app/urls path 연결
3. (make): app/friend/urls.py 만들기
4. (make): friend/view.py 에 index 함수 만들기
5. (make): friend 폴더 내부에 templates/friend 추가
6. (make): templates/friend 내부에 index.html 파일 추가
7. (write): index에 태그작성 (친구추가,친구전체보기)
8. (write): frined/views.py 의 index 함수 수정하기
9. (write): app/setting 에 INSTALLED_APPS 배열안에 "friend.apps.FriendConfig" 추가
10. (write): friend/models.py 모델 작성
<!-- 오타나면 다시만들기 -->
11. (terminal): projects 루트 > python manage.py makemigrations 앱이름
12. (terminal): python manage.py sqlmigrate 앱이름0001 //확인
13. (terminal): python manage.py shell 쉘열기
14. (terminal): from friend.models import Friend 입력
15. (shell): // exit() = shell 나가기
    f = Friend(
    friend_name = '홍길동'
    friend_age = 30
    friend_bigo = '착한아이'
    )

<!-- INSERT문 실행(1) -->

16. (shell):
    f.save()

    {% csrf_token %}

    python manage.py supercreatesuperuser
