from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=255)
