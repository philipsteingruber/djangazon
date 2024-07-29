# Generated by Django 5.0.7 on 2024-07-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_item_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="category",
        ),
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.ManyToManyField(to="base.category"),
        ),
    ]
