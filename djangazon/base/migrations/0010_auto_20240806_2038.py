# Generated by Django A.B on YYYY-MM-DD HH:MM

import django.utils.text
from django.db import migrations, models


def generate_slugs(apps, schema_editor):
    Item = apps.get_model('base', 'Item')
    for item in Item.objects.all():
        item.slug = django.utils.text.slugify(item.name)
        item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0009_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=100, default='', editable=False),
        ),
        migrations.RunPython(generate_slugs),
    ]
