from django import forms
from .models import *

class MovieForm(forms.ModelForm):

    # score = forms.FloatField(
    #     widget=forms.NumberInput(attrs={'type': 'number', 'step': '0.5', 'min': '0', 'max': '5'})
    # )

    # release_date = forms.DateField(
    #         widget=forms.DateInput(attrs={'type': 'date'})
    #     )

    class Meta:
        model = Movie
        exclude = ('user_id', 'like_users',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('user', 'movie', 'main_comment')

