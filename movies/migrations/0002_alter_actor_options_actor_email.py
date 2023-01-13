# Generated by Django 4.1.5 on 2023-01-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actor",
            options={
                "ordering": ["full_name"],
                "verbose_name": "Actor",
                "verbose_name_plural": "Mis Actores",
            },
        ),
        migrations.AddField(
            model_name="actor",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]