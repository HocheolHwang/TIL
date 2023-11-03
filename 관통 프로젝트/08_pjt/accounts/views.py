from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 회원 생성 페이지 조회 & 단일 회원 데이터 생성 (회원가입) (GET & POST)
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인 페이지 조회 & 세션 데이터 생성 및 저장 (로그인) (GET & POST)
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 세션 데이터 삭제 (로그아웃) (GET & POST)
    auth_logout(request)
    return redirect('community:index')


@login_required
def profile(request, username):
    # 사용자 상세 조회 페이지 (프로필 조회) (GET)
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                isFollowed = False
            else:
                person.followers.add(user)
                isFollowed = True
    context = {
        'isFollowed': isFollowed,
        'follwerCount': person.followers.count(),
    }
    return JsonResponse(context)

