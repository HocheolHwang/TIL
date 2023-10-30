from django.db import models



class Actor(models.Model):
    # 배우 데이터 조회
    name = models.CharField(max_length=100)         # 배우 이름


class Movie(models.Model):
    # 영화 데이터 조회
    title = models.CharField(max_length=100)        # 영화 제목
    overview = models.TextField()                   # 줄거리
    release_date = models.DateTimeField()           # 개봉일
    poster_path = models.TextField()                # 포스터 주소
    actors = models.ManyToManyField(Actor, related_name='movies')
    

class Review(models.Model):
    # 리뷰 데이터 조회/생성/수정/삭제
    title = models.CharField(max_length=100)        # 리뷰 제목
    content = models.TextField()                    # 리뷰 내용
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # 외래 키 (Movie)