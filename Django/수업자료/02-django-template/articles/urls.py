from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch, name="catch"),
    # str 기본 값이라 생략 가능
    # path('hello/<str:name>/', views.greeting),
    path('hello/<name>/', views.greeting),
    path('articles/<int:num>/', views.detail),
]
