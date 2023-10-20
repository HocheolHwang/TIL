from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [

    # 분석을 원하는 키워드 입력 및 추가
    path('keyword/', views.keyword, name='keyword'),

    # 키워드 삭제
    path('keyword/<int:pk>/', views.keyword_detail, name="keyword_detail"),

    # 크롤링 수행 및 결과 개수 출력
    path('crawling/', views.crawling,name='crawling'),

    # 크롤링 수행 및 결과 개수 막대 그래프로 출력
    path('crawling/histogram/', views.histogram, name='histogram'),

    # 지난 1년을 기준으로 크롤링 수행 및 결과 개수 막대 그래프 출력
    path('crawling/advanced/', views.advanced, name='advanced'),
]
