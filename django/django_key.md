# 장고에서 쓸만한 것들

## python
- python -m venv venv : 가상 환경 만들기
- python manage.py startapp 앱_이름_복수형 : '앱_이름_복수형'로 앱 생성
- python manage.py runserver : 서버 실행 / ctrl + c로 끄기


## pip
- pip install -r requirements.txt : requirements.txt에 저장된대로 pip install
- pip freeze > requirements.txt : requirements.txt에 환경(가상 환경)에 저장된 것들 기록

## source
- source venv/Scripts/activate : 가상 환경 구동, (venv) 표시로 확인 가능 

## django
- django-admin startproject 프로젝트_이름 . : '프로젝트_이름'으로 프로젝트 폴더 생성/  
  . 하는 게 편함, 없으면 디렉토리 내려가서 작업해야함


## project 폴더
### settings.py
- 앱 등록시키기(**필수**) : 앱 만들고 등록하기
  ```html
  INSTALLED_APPS = [
    '만든 앱 이름',
    ....
  ]
  ```
  
- templates 상위 폴더도 사용하게 설정 : 
  
  뼈대는 app마다 만들어주기보단 project 하나에서 관리하는 게 편함<br> 
  / 상위 폴더에 templates 폴더 만들고 설정하기
  ```html
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        <!-- DiRS에 하단과 같이 객체 지향형으로 적기 -->
        'DIRS': [BASE_DIR / 'templates'],        
        ....
    }]
  ```
- static 폴더 설정 : 이미지, js, css 파일 모아서 사용하는 용도
  /manage.py가 있는 최상위에서 static 폴더 만들어야함
  ```html
  <!-- 디렉토리 만들어서 설정해야함 -->
  STATICFILES_DIRS = [
    BASE_DIR / 'static',
  ]
  ```
### urls.py
- 프로젝트의 urls 대신 앱 urls 사용하도록 조정 <br>
  / 앱 폴더에서 urls.py 만들어야함
  ```html
  <!-- include 추가 -->
  from django.urls import path, include

  <!-- 앱 경로 지정하기 -->
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_apps/', include('first_apps.urls') ),
  ] 
  ```

## templates 폴더 (상위) 
- base.html 생성하기 : 스켈레톤 html 만들기 
- block 설정하기 : 이후 연결된 것들은 block 내부에만 적으면 구동됨
  ```html
    ....
  <style>
      {% block style %}{% endblock style %}
  </style>
  </head>
  <body>
    {% block content %}{% endblock content %}
    ....
  ```
## static 폴더 (최상위)
- css, js, img 다 보관


## apps 폴더
### urls.py
- urls.py 생성 후 동일 폴더 views.py에 연결하기
  ```html
  from django.urls import path
  <!-- 동일 폴더에서 가져오는 건 . 으로 표시 -->
  from . import views

  <!-- html에서 {% url "앱 이름:name" %}로 사용하기 위해 설정 -->
  app_name = '앱 이름'
  urlpatterns = [
      <!-- 기본 페이지 설정, views의 index와 연결, url에서 사용할 이름 설정 -->
      path('', views.index, name='index'),
  ]
  ```
### views.py
- 기본적인 연결 방식
  ```html
  <!-- index라는 class 만들기 -->
  def index(request):
    <!-- 주소는 templates 폴더 내부에 맞게 지정/ templates에 하위폴더 생성함 -->
    return render(request, 'first_apps/index.html')
  ```

## templates (앱 내부)
- 최상위 templates 폴더와 구분되게 앱 이름의 폴더 만들고 그 내부에 html 보관
### views에서 연결한 html 
- base.html을 토대로 html 작업
  ```html
  <!-- 연결할 html -->
  {% extends "base.html" %}

  <!-- 연결된 곳 내부에다가 적기 -->
  {% block style %}{% endblock style %}

  {% block content %}
  <h1>test case</h1>

  {% endblock content %}
  ```
## html
- static 내에 있는 것 활용하기
  ```html
  {% load static %}
  
  {% static "images/logo.png" %}
  ```