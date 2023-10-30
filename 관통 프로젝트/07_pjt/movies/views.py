from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ActorListSerializer, ActorSerializer, MovieSerializer, MovieListSerializer, ReviewSerializer, ReviewListSerializer
from .models import Actor, Movie, Review


@api_view(['GET'])
def actor_list(request):
    # 전체 배우 목록 제공 (GET)
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    # 단일 배우 정보 제공 (출연 영화 제목 포함) (GET)
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)
    

@api_view(['GET'])
def movie_list(request):
    # 전체 영화 목록 제공 (GET)
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    # 단일 영화 정보 제공 (출연 배우 이름과 리뷰 목록 포함) (GET)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

    
@api_view(['GET'])
def review_list(request):
    # 전체 리뷰 목록 제공 (GET)
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    # 단일 리뷰 조회 & 수정 & 삭제 (출연 영화 제목 포함) (GET / PUT / DELETE)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'message': f'review {review_pk} is deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request, movie_pk):
    # 리뷰 생성 (POST)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
