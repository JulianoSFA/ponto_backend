# Generated by Django 3.1.13 on 2021-11-04 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ponto', '0003_auto_20211021_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktime',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_time', to=settings.AUTH_USER_MODEL),
        ),
    ]
