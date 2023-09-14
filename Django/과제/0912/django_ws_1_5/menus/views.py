from django.shortcuts import render
from .data import food, drink

# 문자열이 영어 알파벳으로만 이루어져있는지 확인
def is_english(text):
  for char in text:
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
      return False
  return True


# Create your views here.
def Food(request):
  context = {
    'foods': food
  }
  return render(request, 'menus/food.html', context)


def Drink(request):

  # 리스트 안의 모든 영어 단어의 첫 글자를 대문자로 바꾼다.
  capitalized_drinks = [d[0].upper() + d[1:] for d in drink]
  context = {
    'drinks': capitalized_drinks
  }
  return render(request, 'menus/drink.html', context)


def receipt(request):
  message = request.GET.get('message')
  is_food = request.GET.get('is_food')
  is_in_menu = False

  # food를 주문했다면
  if is_food:
    if message in food:
      is_in_menu = True

  # drink를 주문했다면
  else:
    if is_english(message):
      message = message.lower()

      # 모두 소문자로 바꾼 message가 drink 리스트 안에 있다면,
      # 메뉴 안에 있으므로 is_in_menu를 True로 바꾼다
      if message in drink:
        is_in_menu = True

      # 영어 단어의 첫 글자만 대문자로 바꾼다.
      message = message[0].upper() + message[1:]

  context = {
    'message': message,
    'is_in_menu': is_in_menu,
  }
  return render(request, 'menus/receipt.html', context)