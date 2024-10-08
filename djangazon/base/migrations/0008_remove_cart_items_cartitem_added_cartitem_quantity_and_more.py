# Generated by Django 5.0.7 on 2024-08-06 12:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_alter_cart_user_cartitem"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="items",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="added",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="order",
            name="delivered_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default=User.objects.get(username='philip').id,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="base.cart",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(to="base.cartitem"),
        ),
    ]
