# 장고에서 쓸만한 것들

## python
- python -m venv venv : 가상 환경 만들기
- python manage.py startapp 앱_이름_복수형 : '앱_이름_복수형'로 앱 생성
- python manage.py runserver : 서버 실행 / ctrl + c로 끄기
- python manage.py makemigrations : 설계도(models.py의 class) 최종화
- python manage.py migrate : 설계도대로 DB에 반영
- python manage.py showmigrations : 마이그레이션 잘됬는지 확인용
- python manage.py createsuperuser : 데이터 확인 및 테스트용 관리자 계정 생성

## pip
- pip install -r requirements.txt : requirements.txt에 저장된대로 pip install
- pip freeze > requirements.txt : requirements.txt에 환경(가상 환경)에 저장된 것들 기록

## source
- source venv/Scripts/activate : 가상 환경 구동, (venv) 표시로 확인 가능 

## django
- django-admin startproject 프로젝트_이름 . : '프로젝트_이름'으로 프로젝트 폴더 생성/  
  . 하는 게 편함, 없으면 디렉토리 내려가서 작업해야함
## 기타
- deactivate: 가상환경 중지
- ctrl + c : server 중지

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
- 기본 user 모델 수정 시 필요함 - accounts의 models.py 및 admin 바꿔줘야함
  ```html
  AUTH_USER_MODEL = 'accounts.User'
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
      <!-- 주소를 임의의 값으로 설정,int나 str 등등 다양하게 -->
      path('<int:pk>/', views.detail, name='detail'), 

  ```
### views.py
- 기본적인 연결 방식
  ```html
  <!-- index라는 class 만들기 -->
  def index(request):
    <!-- 주소는 templates 폴더 내부에 맞게 지정/ templates에 하위폴더 생성함 -->
    return render(request, 'first_apps/index.html')
  ```
- 받을게 있을때
  ```html
  def info(request):
    <!-- 받는 data의 이름 꼭 필요, html의 데이터 요청하는법 참고 -->
    data = request.GET.get('message')
    <!-- dictionary 형태로 저장 -->
    context ={
      'whatIWant' = data
    }

    return render(request, 'first_apps/info.html', context)
  
  ```
- DB에 저장된 내용 연결하기
  - 모델의 전체 자료 받아오기
  ```html
  <!-- 전체 받는거니까 변수는 복수형으로 담자 -->
  articles = 받을데이터모델.objects.all()
  context= {
    'data' = articles,
  }  
  ```
  - 특정 자료만 받아오기/ 주소명 별도로 만들어야하니 urls 참조
  ```html
  <!-- urls 주소를 pk로 지정할 것이라 pk 받아와야함 -->
  def detail(request, pk):
      <!-- 특정 정보를 받아오는거니 get 그리고 특정하기 위해 pk 값 받아옴 -->
      article = 받을데이터모델.objects.get(pk=pk)
      context= {
        'article': article,
      }
  ```
#### forms.py로 form 이용
  - 새 데이터 저장하는 방법
    ```html
    from .forms import 갖고올폼이름
    def create(request):
        if request.method = 'POST:
            form = 갖고 올 폼 이름(request.POST)
            if form.is_valid():
                article = form.save()
                <!-- 저장한 내용을 확인하려면 아래와 같이 -->
                return redirect('articles:detail', article.pk)
        else:
            form = 갖고 올 폼 이름()
        context = {
          'form': form,
        }
        return render(reqeust, 'articles/request.html', context)
    ```
- 기존 데이터 삭제:
  ```html
  def delete(request, pk):
      <!-- 삭제할 파일 특정 -->
      article = 삭제할곳의모델이름.objects.get(pk=pk)
      article.delete()
      return redirect('first_apps:index')
  ```
- 기존 데이터 편집을 수정할 때
  ```html
  def update(request, pk):
      article= 저장된모델이름.objects.get(pk=pk)
      if request.method = 'POST:
          form = 모델폼(request.POST, instance= article)
          if form.is_valid():
              <!-- user연결시 commit 내용 추가-->
              article = form.save(commit = false)
              article.user = request.user
              article.save()
              return redirect('first_apps:detail', article.pk)
      else:
          form = 모델폼(instance= article)
      context={
        'article': article,
        'form': form,
      } 
      return render(request, 'first_apps/update.html', context)
  ```
- 로그인 만들기
  ```html
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as logout
  from django.contrib.auth.form import AuthenticationForm
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.method)
          if form.is_valid():
              user = form.get_user()
              auth_login(request, user)
              return redirect('accounts:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      } 
      return render(request, 'accounts/login.html', context)
  ```
- 로그아웃 만들기
  ```html
  def logout(request):
      auth_logout(request)
      return redirect('accounts:index')
  ```

### models.py
- 만들 DB 컨텐츠 만들기, 이후 적용을 위해서 migration 필요
  ```html
  class Article(models.Model):
      want_name = models.CharField(max_length=50)
  ```
- 원하는 대로 USER 설정하기
  ```html
  from django.contrib.auth.models import AbstractUser
  class User(AbstractUser):
      <!-- 수정 안하면 default 값으로 진행됨 -->
      pass
  ```
### admin.py
- 만든 모델을 admin에서 활용하기 위해 연결
  ```html
  from .models import 임포트할_이름

  admin.site.register(임포트할_이름)
  ```
- 유저 모델 수정시
  ```html
  from django.contrib.auth.admin import UserAdmin
  from .models import User

  admin.site.register(User, UserAdmin)
  ```
### forms.py
- 폼을 html 바깥에서 구성시켜 연결
  ```html
  from django import forms
  from .models import MyModel

  <!-- DB에 저장 필요 없는 경우 ex)로그인과 같이 조회만 하는 경우 -->
  class 원하는폼이름(forms.Form):
  <!-- 모델 같이 구성 -->
      title = forms.CharField(max_length= 10)
      <!-- input 외형변경 필요시 widget 사용 -->
      content = forms.CharField(widget=forms.textarea)

  <!-- DB에 저장 혹은 수정 등이 필요한경우 -->
  class 원하는폼이름(forms.ModelForm):
      class Meta:
          model = 연결할 모델 이름
          <!-- 모델 내 전부 다 받을 경우 -->
          fields = '__all__'
          <!-- 일부만 받을 경우 -->
          fields = ('title', etc)
          exclude = ('title', etc)

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

- static 내에 있는 것 활용하기
  ```html
  {% load static %}
  
  {% static "images/logo.png" %}
  ```
- url 이동시키는 법
  ```html
  {% url '앱이름:이름' %}
  ```
- 받은 context dictionary 사용하는 법
  ```html
  <!-- 기본 -->
  {{ context_내부key }}
  <!-- 하위로 들어가기 -->
  {{ key.하위속성 }}
  <!-- 변수 수정방법 -->
  {{ key|filter }}
  {{ key|truncatewords:30 }}
  ```
- 코딩처럼 활용하기
  ```html
  <!-- 적당히 키워드 입력 후 원하는 것 엔터 -->
  {% if  %}{% endif %}
  {% for  in  %}{% endfor %}
  ```
- 데이터 요청하는 법
  ```html
  <!-- form 사용하기 -->
  <form action="보내고싶은주소 ex) /catch/" method='원하는발송방식 ex) GET'>
    <!-- 입력한 데이터에 이름 붙여야함 -->
    <input type="text", id='message', name='message'>
  </form>
  ```
  - forms.py 사용시(forms.py 생성 및 views 설정 필요)
  ```html
  <!-- GET는 단순조회, POST는 생성,삭제 수정시 사용 -->
  <form action="{% url '앱이름:views이름' %}" method="POST">
  {{ form }}
  <!-- DB에 영향을 줄 경우 토큰값도 같이 줘야 허락해줌-->
  {% csrf_token %}
  <input type="submit">
  </form>
  {% endblock content %}
  <!-- form 내부 항목을 p로 감싸는법 -->
  {{ form.as_p }} 
  ```