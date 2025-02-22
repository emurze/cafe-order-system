from django.db import models
from django.urls import reverse


class Dish(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ("slug",)
        indexes = (models.Index(fields=("slug",)),)

    def get_absolute_url(self) -> str:
        return reverse("dishes:detail", args=(self.slug,))

    def __str__(self) -> str:
        return self.title
