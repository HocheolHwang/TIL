from django.db import models
from django.conf import settings


class Movie(models.Model):

    # COMEDY = 'CM'
    # HORROR = 'HR'
    # ROMANCE = 'RM'

    # GENRE_CHOICES = [
    #     (COMEDY, 'Comedy'),
    #     (HORROR, 'Horror'),
    #     (ROMANCE, 'Romance'),
    # ] 

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='like_movies'
    )   

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # audience = models.IntegerField()
    # release_date = models.DateTimeField(null=True)
    # genre = models.CharField(
    #     max_length=2,
    #     choices=GENRE_CHOICES,
    #     default=COMEDY,
    # )
    # score = models.FloatField(null=True)
    # poster_path = models.TextField(null=True)
    # actor_image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 대댓글
    main_comment = models.ForeignKey('self', related_name='sub_comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content