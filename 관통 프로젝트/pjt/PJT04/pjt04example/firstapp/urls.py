from django.urls import path
from . import views
# from 다른앱 import views as views2

# 앱이 하나라면 굳이 app_name 설정 할 필요 없다.
urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]
