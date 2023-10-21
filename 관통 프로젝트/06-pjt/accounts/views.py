from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from .forms import *

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


def update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else :
        form = CustomUserChangeForm(instance=request.user)

    context={
        'form':form
    }
    return render(request, 'accounts/update.html', context)


def resign(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        auth_logout(request)
    return redirect('movies:index')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    
    else :
        form = PasswordChangeForm(request.user)
        context={
            'form':form
        }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username = username)
    context = {
        'person' : person
    }
    
    return render(request, 'accounts/profile.html', context)


def follow(request, user_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    User = get_user_model()
    person = get_object_or_404(User, pk=user_id)
    if request.user != person:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
    

def liked_items(request, user_id):
    like_movie_list = request.user.like_movies.all()
    context = {
        'movie_list': like_movie_list,
        'title': ''
    }
    return render(request, 'accounts/item_list.html', context)


def followers(request, user_id):
    follower_list = request.user.followers.all()
    context = {
        'follower_list': follower_list,
        'title': 'Follower List',
    }
    return render(request, 'accounts/follow_list.html', context)


def followings(request, user_id):
    following_list = request.user.followings.all()
    context = {
        'follow_list': following_list,
        'title': 'Following List',
    }
    return render(request, 'accounts/follow_list.html', context)
    