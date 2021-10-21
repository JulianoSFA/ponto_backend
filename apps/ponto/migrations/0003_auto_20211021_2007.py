# Generated by Django 3.1.13 on 2021-10-21 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0002_remove_worktime_last_time_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worktime',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='worktime',
            name='next_time_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_time', to='ponto.worktime'),
        ),
    ]