from django.contrib import admin

from apps.dishes.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("title",)
