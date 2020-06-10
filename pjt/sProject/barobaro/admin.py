from django.contrib import admin

from .models import User, korean_food, chinese_food, japanese_food


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


class korean_food_Admin(admin.ModelAdmin):
    list_display = ['Restaurant_name']


class chinese_food_Admin(admin.ModelAdmin):
    list_display = ['Restaurant_name']


class japanese_food_Admin(admin.ModelAdmin):
    list_display = ['Restaurant_name']


admin.site.register(User, UserAdmin)
admin.site.register(korean_food, korean_food_Admin)
admin.site.register(chinese_food, chinese_food_Admin)
admin.site.register(japanese_food, japanese_food_Admin)