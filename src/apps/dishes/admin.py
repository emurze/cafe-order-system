from django.contrib import admin

from _dishes_examples.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("title",)
