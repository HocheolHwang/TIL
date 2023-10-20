from django.db import models


class Keyword(models.Model):

    # 검색할 키워드명
    # 데이터 유형: text
    name = models.TextField()

    # 추가된 날짜
    # 데이터 유형: Date
    created_at = models.DateTimeField(auto_now_add=True)


class Trend(models.Model):

    # 검색을 수행한 키워드명
    # 데이터 유형: text
    name = models.TextField()

    # 검색 결과 수
    # 데이터 유형: integer
    result = models.IntegerField()

    # 검색 기간
    # 데이터 유형: text
    search_period = models.TextField()

    # 추가된 날짜
    # 데이터 유형: Date
    created_at = models.DateTimeField(auto_now_add=True)
