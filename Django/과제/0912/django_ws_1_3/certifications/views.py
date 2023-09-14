from django.shortcuts import render
from .data import age, grade

age_lst = list(age[0])

# Create your views here.
def certification1(request):
    context = {
        'name': '배영환',
        'age': age_lst,
        'grade': grade,
    }
    return render(request, 'certifications/certification1.html', context)


def certification2(request):
    context = {
        'name': '황호철',
        'age': age_lst,
        'grade': grade,
    }
    return render(request, 'certifications/certification2.html', context)


def certification3(request):
    context = {
        'name': '원종현',
        'age': age_lst,
        'grade': grade,
    }
    return render(request, 'certifications/certification3.html', context)