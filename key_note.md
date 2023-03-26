### 마이그레이션 외우기 (venv)

python manage.py makemigrations
python manage.py migrate

### 가상환경 실행

python manage.py runserver

<!--가상환경 연결 -->

source venv/bin/activate

<!-- 연결끊기 -->

deactivate

<!-- 프로젝트 만들기 -->

django-admin startproject 프로젝트 이름 .

<!-- 앱만들기 -->

django-admin startapp 앱이름

<!-- 서버죽이기 -->

sudo fuser -k 8000/tcp

<!-- tailwind CDN -->

<script src="https://cdn.tailwindcss.com"></script>

<!-- input 비밀번호 패턴 -->

- 조건
  비밀번호 8자리 이상
  숫자 포함
  영대 문자 포함
  영소 문자 포함
  특수문자 포함
  - pattern="/^(?=._?[A-Z])(?=._?[a-z])(?=._?[0-9])(?=._?[#?!@$%^&*-]).{8,}$/"

<!-- user 토큰 setting 추가 -->

- https://ssungkang.tistory.com/entry/Django-Token-%EC%9D%B8%EC%A6%9D-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-TokenAuthentication

INSTALLED_APPS = [
'rest_framework.authtoken',
]
