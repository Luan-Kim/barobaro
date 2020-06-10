from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class korean_food(models.Model):
    Restaurant_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'kor_food'

    def __str__(self):
        return self.Restaurant_name


class chinese_food(models.Model):
    Restaurant_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'cn_food'

    def __str__(self):
        return self.Restaurant_name


class japanese_food(models.Model):
    Restaurant_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'jp_food'

    def __str__(self):
        return self.Restaurant_name
