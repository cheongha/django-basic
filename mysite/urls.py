# 1 라우팅
from django.contrib import admin
from django.urls import include, path

# http://ip주소:포트번호/polls/test 라면 polls 폴더의 urls.py로
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]