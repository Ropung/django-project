`프로젝트 만들기`
django-admin startproject 프젝이름 .
`앱만들기`
django-admin startapp 앱이름
`가상환경 (연결,실행,해제)`
source venv/bin/activate
deactivate
`서버 실행`
python manage.py runserver
`마이그레이션`
python manage.py makemigrations
python manage.py migrate
`슈퍼 유저생성`
python manage.py supercreatesuperuser
사용자이름 : admin
이메일 주소: admin@admin.com
비밀번호 : admin
`setting`
(mac): import pymysql
(mac): pymysql.install_as_MySQLdb()
APPEND_SLASH = False
`INSTALLED_APPS 설정`
INSTALLED_APPS = [
"앱이름.apps.앱이름Config",
]
`TEMPLATES 설정`
"DIRS": [BASE_DIR/'templates'],
`언어설정`
LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = False
`STATIC 경로설정`
STATIC_URL = "static/"
STATICFILES_DIRS = [
BASE_DIR / 'static',
]
`[리다이렉트 로그인 로그아웃]`
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
`파일 업로드 관련`
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
`tailwind CDN`
src="https://cdn.tailwindcss.com"
`서버죽이기`
sudo fuser -k 8000/tcp

`extends`
{% extends 'common/base.html' %}
{% block title %}[게시판]{% endblock title %}
{% block body %}

# db 연결설정 파일

[client]
datebase=mydb
user=root
password=root
host=127.0.0.1
port=3306
default-charset=utf-8

범위: django 프로젝트 만들기 앱만들기 , model 생성하기(migrations) , MVT패턴, urls.py, settings.py, views.py, 템플릿태그(include, 템플릿상속없음), javascript, ajax
