from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('korean_food/', views.kor_food, name='korean food'),
    path('japanese_food/', views.jp_food, name='japanese food'),
    path('chinese_food/', views.cn_food, name='chinese food'),
    path('order/', views.order, name='order'),
    path('menu/', views.menu, name='menu'),
]