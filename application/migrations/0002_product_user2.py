# Generated by Django 3.2.9 on 2023-07-05 12:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user2',
            field=models.ManyToManyField(default=None, related_name='user2_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
