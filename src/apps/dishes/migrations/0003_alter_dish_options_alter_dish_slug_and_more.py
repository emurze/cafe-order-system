# Generated by Django 5.1.6 on 2025-02-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dishes", "0002_dish_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ("slug",), "verbose_name_plural": "Dishes"},
        ),
        migrations.AlterField(
            model_name="dish",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddIndex(
            model_name="dish",
            index=models.Index(
                fields=["slug"], name="dishes_dish_slug_f32b8f_idx"
            ),
        ),
    ]
