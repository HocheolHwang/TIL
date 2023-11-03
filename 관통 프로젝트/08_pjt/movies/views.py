from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Genre, Movie


@require_safe
def index(request):
    # 전체 영화 목록 페이지 조회 (GET)
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    # 단일 영화 상세 페이지 조회 (GET)
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()  # 해당 영화의 모든 장르 가져오기
    context = {
        'movie': movie,
        'genres': genres
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    # 추천 영화 페이지 조회 (GET)
    # 인기도가 높은 상위 10개의 영화를 추천 목록으로 전달
    recommended_movies = Movie.objects.order_by('-popularity')[:10]
    context = {
        'recommended_movies': recommended_movies
    }
    return render(request, 'movies/recommended.html', context)
