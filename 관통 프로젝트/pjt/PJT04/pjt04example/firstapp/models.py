from django.db import models
from django.contrib.auth.models import AbstractUser


# Django가 기본적으로 User 모델을 갖고 있는데
# 왜 덮어써야 하는가?
# 1. Django 권장사항
# 2. 커스텀을 하기 위해서

class User(AbstractUser):
    pass
